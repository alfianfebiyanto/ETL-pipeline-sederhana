import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def format_alert(severity: str, time: str, job: str, stage: str, message: str) -> str:
    """
    Bikin teks alert yang rapi & konsisten.
    severity: ERROR/WARN/INFO
    stage: precheck/extract/transform/load/runtime
    """
    
    return f"""
    <html>
      <body>
        <p>&#128680;  <b>ALERT [{severity}]</b> &#128680;</p>
        <p><b>Job : </b> {job}</p>
        <p><b>Stage : </b> {stage}</p>
        <p><b>Time : </b> {time}</p>
        <hr>
        <p><b>Error Message : </b></p>
        <pre>{message}</pre>
        <hr>
        <p><i>Note : Segera periksa log ETL untuk investigasi.</i></p>
      </body>
    </html>
    """

def send_email_alert(subject: str, body: str, sender: str,app_password: str, to: str):
    """
    kirim email via Gmail SMTP (SSL 465)
    """
    msg = MIMEText(body,'HTML','utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=15) as s:
        s.login(sender, app_password)
        s.send_message(msg)