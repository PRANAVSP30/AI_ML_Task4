import pandas as pd

# ----------------------------------------------------
# 1. Clean unwanted spaces / formatting from text columns
# ----------------------------------------------------
def clean_text_columns(df):
    """
    Strips extra spaces from all text columns.
    Example: ' Private ' -> 'Private'
    """
    df_cleaned = df.copy()
    obj_cols = df_cleaned.select_dtypes(include=['object']).columns

    for col in obj_cols:
        df_cleaned[col] = df_cleaned[col].astype(str).str.strip()

    return df_cleaned


# ----------------------------------------------------
# 2. Standardize column names
# Converts to lowercase, replaces spaces/hyphens with underscore
# ----------------------------------------------------
def standardize_column_names(df):
    """
    Converts column names into machine-friendly format:
    'Marital-Status' -> 'marital_status'
    'Native Country' -> 'native_country'
    """
    df_cleaned = df.copy()
    df_cleaned.columns = (
        df_cleaned.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df_cleaned
