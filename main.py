from config.setting import USER_PATH ,PRODUCT_PATH, TRANSCATION_PATH ,OUTPUT_PATH
from scripts.ekstract import exctract_csv, extract_json
from scripts.transform import transform_data
from scripts.load import save_to_csv

# Extract
product_df = exctract_csv(PRODUCT_PATH)
transaction_df = exctract_csv(TRANSCATION_PATH)
user_df = extract_json(USER_PATH)

# Transform
final_df = transform_data(product_df,transaction_df,user_df)

# Load 
save_to_csv(final_df, OUTPUT_PATH)
print(f'ETL selesai file disimapn disini {OUTPUT_PATH}')