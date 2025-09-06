#!/usr/bin/env python3
"""
autoinsight.py: A command-line tool that provides automated insights from a CSV dataset.
Usage: python autoinsight.py --file <path_to_csv> [--verbose]
python autoinsight.py --file ../data/iris.csv

This tool loads a CSV file and generates insights like summary statistics, data types,
missing values, and correlations with minimal user input.
"""

import argparse
import sys

import pandas as pd


def load_dataset(file_path):
    """Load the CSV dataset and handle basic errors."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)


def generate_insights(df, verbose=False):
    """Generate and print insights from the DataFrame."""
    print("\n=== Dataset Insights ===")

    # Basic Info
    print("\n1. Dataset Overview:")
    print(f" - Number of rows: {df.shape[0]}")
    print(f" - Number of columns: {df.shape[1]}")
    print(f" - Column names: {', '.join(df.columns)}")

    # Data Types
    print("\n2. Data Types:")
    for col, dtype in df.dtypes.items():
        print(f" - {col}: {dtype}")

    # Missing Values
    missing = df.isnull().sum()
    print("\n3. Missing Values:")
    for col, count in missing.items():
        print(f" - {col}: {count} ({(count / df.shape[0]) * 100:.2f}%)")

    # Summary Statistics (for numeric columns)
    print("\n4. Summary Statistics (Numeric Columns):")
    numeric_df = df.select_dtypes(include=["number"])
    if not numeric_df.empty:
        print(numeric_df.describe().to_string())
    else:
        print(" - No numeric columns found.")

    # Unique Values (verbose mode only, to keep minimal input light)
    if verbose:
        print("\n5. Unique Values per Column:")
        for col in df.columns:
            unique_count = df[col].nunique()
            print(f" - {col}: {unique_count} unique values")

    # Correlations (for numeric columns, verbose mode)
    if verbose and not numeric_df.empty:
        print("\n6. Correlation Matrix:")
        print(numeric_df.corr().to_string())

    print("\n=== End of Insights ===")


def main():
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(
        description="AutoInsight: Generate insights from a CSV dataset with minimal input."
    )
    parser.add_argument("--file", required=True, help="Path to the CSV dataset file.")
    parser.add_argument(
        "--verbose", action="store_true", help="Enable verbose output (more details)."
    )
    args = parser.parse_args()

    # Load data
    df = load_dataset(args.file)

    # Generate insights
    generate_insights(df, verbose=args.verbose)


if __name__ == "__main__":
    main()
