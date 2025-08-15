import pandas as pd

def transform_data(product_df,transaction_df,user_df):

    # Dataframe Product
    product_df['currency'] = product_df['price'].str[:2]
    product_df['price'] = product_df['price'].str[3:].astype(int)

    # Dataframe Transactions
    transaction_df['transaction_date'] = pd.to_datetime(transaction_df['transaction_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    #Dataframe User
    user_df['email'] = user_df['email'].replace("",None)

    return user_df.head(10)
