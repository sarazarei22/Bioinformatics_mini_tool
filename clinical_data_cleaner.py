import numpy as np
import pandas as pd


def clean_clinical_data(file_path: str) -> pd.DataFrame:
  """Cleans clinical trial dataset by handling missing values,

  standardizing column names, and filtering out outliers.

  Parameters:
      file_path (str): Path to the CSV data file.

  Returns:
      pd.DataFrame: Cleaned and standardized dataframe.
  """
  # Load dataset (Simulated path for demonstration)
  df = pd.read_csv(file_path)

  # 1. Standardize column names (lowercase and strip spaces)
  df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

  # 2. Handle missing values in critical numeric columns (e.g., age, blood pressure)
  if 'age' in df.columns:
    df['age'] = df['age'].fillna(df['age'].median())

  if 'blood_pressure' in df.columns:
    df['blood_pressure'] = df['blood_pressure'].fillna(
        df['blood_pressure'].mean()
    )

  # 3. Drop rows where patient ID or critical diagnosis is missing
  if 'patient_id' in df.columns:
    df = df.dropna(subset=['patient_id'])

  # 4. Remove logical outliers (e.g., impossible age values)
  if 'age' in df.columns:
    df = df[(df['age'] >= 0) & (df['age'] <= 120)]

  print(
      f'Data cleaning complete. Cleaned dataset shape: {df.shape[0]} rows,'
      f' {df.shape[1]} columns.'
  )
  return df


if __name__ == '__main__':
  # Example execution block
  print('Clinical Data Cleaner script loaded successfully.')
