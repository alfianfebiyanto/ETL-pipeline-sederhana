
from datetime import date
from config.setting import ALERT_EMAIL_SENDER, ALERT_EMAIL_APP_PASSWORD, ALERT_EMAIL_TO
from scripts.monitoring import summarize_today   # ini mengacu ke scripts/report.py (monitoring)
from scripts.alerts import send_email_alert

def main():
    html, msg = summarize_today()
    if msg:
        html = f"<html><body><p>{msg}</p></body></html>"
    
    send_email_alert(
        subject=f"[REPORT] ETL Daily Summary — {date.today().isoformat()}",
        body=html,
        sender=ALERT_EMAIL_SENDER,
        app_password=ALERT_EMAIL_APP_PASSWORD,
        to=ALERT_EMAIL_TO,
    )

if __name__ == "__main__":
    main()