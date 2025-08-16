import smtplib
from email.mime.text import MIMEText

def format_alert(severity: str, run_id: str, job: str, stage: str, message: str) -> str:
    """
    Bikin teks alert yang rapi & konsisten.
    severity: ERROR/WARN/INFO
    stage: precheck/extract/transform/load/runtime
    """
    return(
        f"[{severity}] {job} ({stage}) | run_id={run_id}\n"
        f"{message}\n"
    )

def send_email_alert(subject: str, body: str, sender: str,app_password: str, to: str):
    """
    kirim email via Gmail SMTP (SSL 465)
    """
    msg = MIMEText(body,'plain','utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=15) as s:
        s.login(sender, app_password)
        s.send_message(msg)