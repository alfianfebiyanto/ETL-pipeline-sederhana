from config.setting import USER_PATH ,PRODUCT_PATH, TRANSCATION_PATH
from scripts.ekstract import exctract_csv, extract_json
from scripts.transform import transform_data

# Extract
product_df = exctract_csv(PRODUCT_PATH)
transaction_df = exctract_csv(TRANSCATION_PATH)
user_df = extract_json(USER_PATH)

# Transform
transformed_df = transform_data(product_df)
print(transformed_df)