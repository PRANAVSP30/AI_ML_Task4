import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# ----------------------------------------------------
# 1. Detect numerical columns
# ----------------------------------------------------
def detect_numerical(df):
    numerical = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    return numerical


# ----------------------------------------------------
# 2. Standard Scaling (Mean=0, Std=1)
# ----------------------------------------------------
def apply_standard_scaling(df, columns):
    df_scaled = df.copy()
    scaler = StandardScaler()
    df_scaled[columns] = scaler.fit_transform(df_scaled[columns])
    return df_scaled, scaler


# ----------------------------------------------------
# 3. Min-Max Scaling (0 to 1)
# ----------------------------------------------------
def apply_minmax_scaling(df, columns):
    df_scaled = df.copy()
    scaler = MinMaxScaler()
    df_scaled[columns] = scaler.fit_transform(df_scaled[columns])
    return df_scaled, scaler


# ----------------------------------------------------
# 4. Scaling report for comparison
# ----------------------------------------------------
def scaling_report(df_before, df_after, columns):
    report = {}
    for col in columns:
        report[col] = {
            "Before Min": df_before[col].min(),
            "Before Max": df_before[col].max(),
            "After Min": df_after[col].min(),
            "After Max": df_after[col].max()
        }
    return report


# ----------------------------------------------------
# 5. Save scaled data to CSV
# ----------------------------------------------------
def save_scaled_data(df, path):
    df.to_csv(path, index=False)
    return True
