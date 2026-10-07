import os
import pandas as pd
import numpy as np


DATA_URL = (
    "https://raw.githubusercontent.com/"
    "dibyendubiswas1998/Crop-Production-Analysis/"
    "main/DATA/crop_production.csv"
)


def load_data():
    """
    Load agricultural crop production data
    from a public GitHub dataset.
    """

    print("\nLoading agricultural dataset...")

    df = pd.read_csv(DATA_URL)

    print(f"Original dataset shape: {df.shape}")
    print("\nColumns:")
    print(df.columns.tolist())

    return df


def clean_data(df):
    """
    Clean and prepare agricultural data.
    """

    print("\nStarting data cleaning...")

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
    )

    # Convert numerical columns
    numeric_columns = [
        "Crop_Year",
        "Area",
        "Production"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # Remove rows with missing important values
    required_columns = [
        "State_Name",
        "District_Name",
        "Crop_Year",
        "Season",
        "Crop",
        "Area",
        "Production"
    ]

    df = df.dropna(
        subset=required_columns
    )

    # Remove negative area values
    df = df[df["Area"] >= 0]

    # Remove negative production values
    df = df[df["Production"] >= 0]

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean text columns
    text_columns = [
        "State_Name",
        "District_Name",
        "Season",
        "Crop"
    ]

    for column in text_columns:
        if column in df.columns:
            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
            )

    # Reset index
    df = df.reset_index(drop=True)

    print(f"Cleaned dataset shape: {df.shape}")

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    return df


def save_cleaned_data(df):
    """
    Save cleaned agricultural dataset.
    """

    output_directory = "data"

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    output_path = os.path.join(
        output_directory,
        "cleaned_agriculture_data.csv"
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"\nCleaned dataset saved to: {output_path}"
    )

    return output_path