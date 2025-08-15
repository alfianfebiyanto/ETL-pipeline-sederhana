from config.setting import USER_PATH ,PRODUCT_PATH, TRANSCATION_PATH
from scripts.transform import transform_csv

# Extract
user_df = transform_csv(PRODUCT_PATH)
print(user_df)