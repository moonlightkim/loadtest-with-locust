import pandas as pd

def readjson(filepath: str):
    return pd.read_json(filepath)