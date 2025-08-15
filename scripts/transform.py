
import pandas as pd

def transform_csv(path):
    return pd.read_csv(path)

def transform_json(path):
    return pd.read_json(path)
