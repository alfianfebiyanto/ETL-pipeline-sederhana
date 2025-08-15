def transform_data(product_df),transaction_df:

    # Data Frame Product
    product_df['currency'] = product_df['price'].str[:2]
    product_df['price'] = product_df['price'].str[3:].astype(int)

    return product_df.head(5)
