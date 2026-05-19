import pandas as pd
from utils import(clean_columns,remove_duplicates,create_profit_margin)

import os

print(os.getcwd())
# Extrair
df = pd.read_csv("data/raw/superstore.csv", encoding="latin1")


# Transformar
df = clean_columns(df)
df = remove_duplicates(df)
df = create_profit_margin(df)

#Carregar
df.to_csv('data/processed/superstore_clean.csv', index=False)

print("Etl Completo")