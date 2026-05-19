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

def create_profit_margin(df):
    df['profit_margin'] = df['profit']/df['sales']
    return df