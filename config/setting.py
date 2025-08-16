from pathlib import Path
import os
from dotenv import load_dotenv

# Path Base Project
BASE_DIR =Path(__file__).resolve().parent.parent

# ===== LOAD ENV FILE =====
load_dotenv(BASE_DIR/".env")

# ===== EMAIL ALERT CONFIG =====
ALERT_EMAIL_SENDER = os.getenv("ALERT_EMAIL_SENDER")
ALERT_EMAIL_APP_PASSWORD = os.getenv("ALERT_EMAIL_APP_PASSWORD")
ALERT_EMAIL_TO = os.getenv("ALERT_EMAIL_TO",ALERT_EMAIL_SENDER)

# ===== PATH FILE INPUT =====
PRODUCT_PATH ="data/products.csv"
TRANSCATION_PATH ="data/transactions.csv"
USER_PATH ="data/users.json"

# ===== PATH FILE OUTPUT =====
OUTPUT_PATH = "warehouse/fact_sales.csv"

