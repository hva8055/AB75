# Attendance Alert System

A Flask-based web application that automates sending email alerts to students whose attendance is below 75%. The application supports both CSV and Excel file formats.

## Features
- Upload attendance files (CSV or Excel).
- Automatically calculates attendance and identifies students with less than 75% attendance.
- Sends personalized email alerts with the list of subjects where attendance is low.
- Supports multiple subjects and dynamically adjusts to the input data.

## Prerequisites
- Python 3.x
- Flask
- Pandas
- openpyxl (for Excel file support)
- smtplib (for sending emails)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hva8055/AB75.git
   cd attendance-alert
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Update your email credentials in the `app.py` file:
```python
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-email-password"
```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
3. Upload the attendance file (CSV or Excel).
4. Click "Proceed" to analyze and send attendance alert emails.

## Folder Structure
```
attendance-alert/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to contribute to this project by submitting a pull request or reporting issues.

## Acknowledgments
Special thanks to everyone who contributed to this project.
