def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )
    return df

def remove_duplicates(df):
    return df.drop_duplicates()

def round(df, column, decimals=2):
    df[column] = df[column].astype(float).round(decimals)
    return df