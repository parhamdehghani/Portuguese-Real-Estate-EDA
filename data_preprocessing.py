import pandas as pd
import numpy as np

def clean_data(df):
    # Handle missing values
    df = df.dropna(subset=['Price', 'District', 'Type'])
    df['PublishDate'] = pd.to_datetime(df['PublishDate'], errors='coerce')
    area_columns = ['GrossPrivateArea', 'UsableArea', 'LivingArea', 'LotSize', 'BuiltArea']
    df[area_columns] = df[area_columns].apply(pd.to_numeric, errors='coerce')
    df['EnergyCertificate'] = df['EnergyCertificate'].fillna('Unknown')
    return df

def engineer_features(df):
    # Price per square meter calculation
    df['PricePerSqMeter'] = df['Price'] / df['UsableArea']
    df['PricePerSqMeter'].fillna(df['PricePerSqMeter'].median(), inplace=True)

    # Property age calculation
    df['Age'] = 2024 - df['ConstructionYear']
    df['Age'] = df['Age'].replace({2024: None})  # Replace for missing values
    return df

