import pandas as pd

def exctract_csv(path):
    return pd.read_csv(path)

def extract_json(path):
    return pd.read_json(path)