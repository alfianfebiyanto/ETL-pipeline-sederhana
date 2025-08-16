import csv, time
from datetime import datetime, date
from pathlib import Path
from collections import Counter

METRICS_CSV = Path("report/etl_report.csv")

def start_timer():
    return time.time()

def stop_timer(t0):
    return round(time.time() - t0,2)

def make_matrics(time, status, stage,
                t0, source_rows=0, transformed_rows=0,
                loaded_rows=0, error_message=""):
    
    return {
        "time": time,
        "date": date.today().isoformat(),
        "start_time": datetime.fromtimestamp(t0).isoformat(timespec="seconds"),
        "end_time": datetime.now().isoformat(timespec="seconds"),
        "status": status,
        "stage": stage,
        "source_rows": int(source_rows),
        "transformed_rows": int(transformed_rows),
        "loaded_rows": int(loaded_rows),
        "error_message":(error_message or ""[:300])
    }

def log_run(metrics: dict):
    METRICS_CSV.parent.mkdir(parents=True, exist_ok=True)
    is_new = not METRICS_CSV.exists()
    with METRICS_CSV.open("a",newline="",encoding="utf-8") as f:
        w =csv.DictWriter(f, fieldnames=list(metrics.keys()))
        if is_new:
            w.writeheader()
        w.writerow(metrics)
    
def summarize_today():
    if not METRICS_CSV.exists():
        return None, "No runs yet."
    
    rows = []
    with METRICS_CSV.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r['date'] == date.today().isoformat():
                rows.append(r)
    if not rows:
        return None,"No runs today."

    cnt = Counter(r["status"] for r in rows)
    total = len(rows)
    ok = cnt.get("SUCCES", 0)
    fail = cnt.get("FAILED",0)
    avg_dur = sum(float(r.get("duration_sec",0.0)) for r in rows) / total
    total_loaded = sum(int(r.get("Loaded_rows") or 0) for r in rows)

    html = f"""
    <html><body> 
        <h3>ETL Daily Report — {date.today().isoformat()}</h3>
            <ul>
                <li><b>Total runs : </b> {total} ({ok} | {fail})</li>
                <li><b>Avg duration : </b> {avg_dur:.2f}s</li>
                <li><b>Total loaded rows : </b> {total_loaded}</li>
            </ul>
        <hr>
        <p><i>Note: Data diambil dari monitoring/etl_rusns.csv</i></p>
    <body></html>
    """
    return html, None