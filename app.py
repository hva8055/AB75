import pandas as pd
from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  

EMAIL_ADDRESS = "your Email"
EMAIL_PASSWORD = "Your App Password"

def read_file(file):
    """Read CSV or Excel file based on extension."""
    if file.filename.endswith('.csv'):
        return pd.read_csv(file)
    elif file.filename.endswith(('.xls', '.xlsx')):
        return pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Check if files are in the request
        if 'attendance_file' not in request.files or 'email_file' not in request.files:
            return "Please upload both attendance and email files."

        attendance_file = request.files['attendance_file']
        email_file = request.files['email_file']

        # Read attendance and email data
        try:
            attendance_df = read_file(attendance_file)
            email_df = read_file(email_file)
        except ValueError as e:
            return str(e)

        # Drop the first row and keep necessary columns
        c = attendance_df.drop(index=0)
        att = pd.DataFrame()
        att['Name'] = c['Name']
        att['Roll No'] = c['Roll No']

        # Extract attendance columns dynamically
        for i in range(5, 20, 3):
            s = f"Unnamed: {i}"
            try:
                att[i] = c[s]
            except KeyError:
                break

        # Get column names and rename columns
        cc = attendance_df.columns
        c_n = ['Name', 'Roll No']
        for i in range(3, 20, 3):
            try:
                c_n.append(cc[i])
            except IndexError:
                break
        att.columns = [c_n]

        # Convert attendance columns to float
        for i in att.columns:
            try:
                att[i[0]] = att[i[0]].astype(float)
            except ValueError:
                continue

        # Filter students with attendance below 75% in any subject
        try:
            below_75 = att[(att.iloc[:, 2:] < 75).any(axis=1)]
        except TypeError:
            pass

        # Flatten multi-level columns
        below_75.columns = ['_'.join(col) if isinstance(col, tuple) else col for col in below_75.columns]

        # Merge email data with attendance data
        merge = pd.merge(email_df, below_75, on='Roll No', how='inner')
        cp = merge.columns
        ind = 0
        cn = []
        for i in cp:
            if(i=='Email' or i=='EMAIL'):
                cn.append('email')
            else:
                cn.append(i) 
        ind+=1
        merge.columns = cn

        # Send attendance alert emails
        for index, row in merge.iterrows():
            low_attendance_subjects = [f"{col}: {row[col]}%" for col in merge.columns[3:] if row[col] < 75]
            subject = "Attendance Alert"
            body = f"Dear {row['Name']},\n\nYour attendance is below 75% in the following subjects:\n\n"
            body += "\n".join(low_attendance_subjects)
            body += "\n\nPlease take necessary action."

            receiver_email = row['email']

            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = receiver_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())
                server.quit()
                print(f"Email sent successfully to {receiver_email}")
            except Exception as e:
                print(f"Error sending email to {receiver_email}: {e}")

        return "Emails sent successfully!"

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
