import pandas as pd
from utils import(clean_columns,remove_duplicates,round)

import os

print(os.getcwd())
# Extrair
df = pd.read_csv("data/raw/superstore.csv", encoding="latin1")


# Transformar
df = clean_columns(df)
df = remove_duplicates(df)
df = round(df, "sales", 2)
df = round(df, "discount", 2)
df = round(df, "profit", 2)

#Carregar
df.to_csv('data/processed/superstore_clean.csv', index=False)

print("Etl Completo")