from datetime import datetime
import traceback

from config.setting import (
    USER_PATH ,PRODUCT_PATH, TRANSCATION_PATH ,OUTPUT_PATH,
    ALERT_EMAIL_APP_PASSWORD, ALERT_EMAIL_SENDER, ALERT_EMAIL_TO
)
from scripts.ekstract import exctract_csv, extract_json
from scripts.transform import transform_data
from scripts.load import save_to_csv
from scripts.alerts import send_email_alert, format_alert

JOB_NAME = 'ETL_Sederhana'

def run_etl():
    # Extract
    product_df = exctract_csv(PRODUCT_PATH)
    transaction_df = exctract_csv(TRANSCATION_PATH)
    user_df = extract_json(USER_PATH)

    # Transform
    final_df = transform_data(product_df,transaction_df,user_df)

    # Load 
    save_to_csv(final_df, OUTPUT_PATH)
    print(f'ETL selesai file disimapn disini {OUTPUT_PATH}')

if __name__=="__main__":
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    try:
        # (opsional) nanti kita tambah prechecks() disini
        raise RuntimeError("TEST ALERT: sengaja gagal untuk cek email.")
        run_etl()
    except Exception:
        err = traceback.format_exc()
        body = format_alert(
            severity="ERROR",
            run_id=run_id,
            job=JOB_NAME,
            stage="runtime",
            message=err
        )
        # kirim email alert
        try:
            send_email_alert(
                subject=f"[ALERT] {JOB_NAME} FAILED {run_id}",
                body=body,
                sender=ALERT_EMAIL_SENDER,
                app_password=ALERT_EMAIL_APP_PASSWORD,
                to=ALERT_EMAIL_TO,
            )
        finally:
            # tetp raise biar bisa ketahuan gagal di scheduler/log
            raise
        