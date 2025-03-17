Attendance Alert System
A Flask-based web application to automate sending attendance alert emails to students whose attendance is below 75%. The application accepts either a CSV or Excel file containing attendance data and sends personalized emails to students who have low attendance in one or more subjects.

🚀 Features
Upload CSV or Excel files for attendance data.
Automatically detects subjects with attendance below 75%.
Sends personalized emails to each student mentioning the subjects with low attendance.
Supports both .csv and .xlsx file formats.
User-friendly web interface built with Flask.
🛠️ Technologies Used
Python
Flask
Pandas
SMTP (for sending emails)
📂 Project Structure
csharp
Copy
Edit
attendance-alert/
├── app.py               # Main Flask application
├── templates/
│   └── index.html        # Web interface
├── uploads/              # Uploaded files storage
└── README.md             # Project documentation
📝 Prerequisites
Python 3.x
Flask
Pandas
Openpyxl (for Excel file support)
💻 Installation
Clone the repository:
bash
Copy
Edit
git clone https://github.com/username/attendance-alert.git
cd attendance-alert
Set up your email credentials in app.py:
python
Copy
Edit
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
🚀 Running the Application
Start the Flask server:
nginx
Copy
Edit
python app.py
Open your browser and visit:
cpp
Copy
Edit
http://127.0.0.1:5000
Upload a CSV or Excel file and click "Proceed" to send attendance alert emails.
📧 Email Format
The email sent to each student will be formatted as follows:

yaml
Copy
Edit
Subject: Attendance Alert

Dear [Student Name],

Your attendance is below 75% in the following subjects:
- Course 1: 70%
- Course 2: 65%
- Course 3: 68%

Please take necessary action.
📝 CSV/Excel Format
Your input file should contain the following columns:

Name: Student's name
Roll No: Student's roll number
Course 1, Course 2, Course 3, ...: Attendance percentages
💡 Troubleshooting
Length Mismatch Error:
Ensure that the number of columns in your file matches the number of column names being assigned.

400 Bad Request:
Make sure your file upload form is correctly formatted and the file is properly selected.

Email Sending Issues:
Verify that your email and password are correct and allow less secure apps in your Gmail settings.

📝 License
This project is licensed under the MIT License.

💬 Contact
For any questions or suggestions, feel free to reach out!
Happy Coding! 🚀
