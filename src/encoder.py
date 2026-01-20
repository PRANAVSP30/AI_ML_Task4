import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# ----------------------------------------------------
# 1. Detect categorical and numerical features
# ----------------------------------------------------
def detect_feature_types(df):
    numerical = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical = df.select_dtypes(include=['object']).columns.tolist()
    return numerical, categorical


# ----------------------------------------------------
# 2. Apply Label Encoding
# ----------------------------------------------------
def apply_label_encoding(df, columns):
    df_encoded = df.copy()
    le = LabelEncoder()
    for col in columns:
        df_encoded[col] = le.fit_transform(df_encoded[col])
    return df_encoded


# ----------------------------------------------------
# 3. Apply One-Hot Encoding
# ----------------------------------------------------
def apply_one_hot_encoding(df, columns):
    df_encoded = pd.get_dummies(df, columns=columns, drop_first=True)
    return df_encoded


# ----------------------------------------------------
# 4. Automatic Encoding (Smart)
# ----------------------------------------------------
def auto_encode(df):
    df_copy = df.copy()

    numerical, categorical = detect_feature_types(df_copy)

    label_cols = []
    onehot_cols = []

    for col in categorical:
        unique_count = df_copy[col].nunique()
        
        # label encode if categorical values <= 10
        if unique_count <= 10:
            label_cols.append(col)
        else:
            onehot_cols.append(col)

    # Step A: Label encoding
    df_copy = apply_label_encoding(df_copy, label_cols)

    # Step B: One-hot encoding
    df_copy = apply_one_hot_encoding(df_copy, onehot_cols)

    return df_copy, label_cols, onehot_cols
