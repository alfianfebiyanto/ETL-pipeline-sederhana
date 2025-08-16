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
from scripts.monitoring import start_timer, stop_timer, make_matrics, log_run

JOB_NAME = 'ETL_Sederhana_Project'

if __name__=="__main__":
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    stage = "start"
    t0 = start_timer()
        
    try:
        
        # Extract
        stage= "Extract"
        product_df = exctract_csv(PRODUCT_PATH)
        transaction_df = exctract_csv(TRANSCATION_PATH)
        user_df = extract_json(USER_PATH)

        # Transform
        stage= "Transfrom"
        final_df = transform_data(product_df,transaction_df,user_df)

        # Load 
        stage= "Load"
        save_to_csv(final_df, OUTPUT_PATH)
        print(f'ETL selesai file disimpan disini {OUTPUT_PATH}')
    
        # Log Sukses
        metrics = make_matrics(
            time=time_stamp,
            status="Sucsses",
            stage=stage,
            t0=t0,
            source_rows=len(transaction_df),
            transformed_rows=len(final_df),
            loaded_rows=len(final_df)
        )
        log_run(metrics)


    except Exception: 
        err = traceback.format_exc() 
        
        # Log Failed
        metrics = make_matrics(
            time=time_stamp,
            status="Failed",
            stage=stage,
            t0=t0,
            source_rows=len(transaction_df),
            transformed_rows=len(final_df),
            loaded_rows=len(final_df)
        )
        log_run(metrics)

        body = format_alert( # body = # struktur alert  pesan ditulis disini
            severity="WARNING",
            time=time_stamp,
            job=JOB_NAME,
            stage=stage,
            message=err
        ) 
        
        try:
            send_email_alert( # ini function arlet yang dikirim ke email kita
                subject=f"[ALERT] {JOB_NAME} FAILED {time_stamp}", # subkect yang dikirim sama email kita
                body=body, # ini diambil dari body diatas
                sender=ALERT_EMAIL_SENDER, 
                app_password=ALERT_EMAIL_APP_PASSWORD,
                to=ALERT_EMAIL_TO,
            )
        finally:
            # tetap raise biar bisa ketahuan gagal di scheduler/log
            raise
        