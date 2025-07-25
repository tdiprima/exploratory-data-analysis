import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Read the CSV file
df = pd.read_csv('visit_occurrence.csv')

# Basic information about the dataset
print("=== DATASET OVERVIEW ===")
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nColumn names and types:")
print(df.dtypes)
print(f"\nMissing values per column:")
print(df.isnull().sum())

# Convert datetime columns to proper datetime type
date_columns = ['visit_start_datetime', 'visit_end_datetime']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Basic statistics for numeric columns
print("\n=== NUMERIC COLUMNS STATISTICS ===")
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
print(df[numeric_cols].describe())

# Analyze visit patterns
print("\n=== VISIT PATTERNS ===")
print(f"Unique patients: {df['person_id'].nunique()}")
print(f"Unique visit types: {df['visit_concept_id'].nunique()}")
print(f"Unique care sites: {df['care_site_id'].nunique()}")

# Top 10 most common visit types
print("\nTop 10 visit types:")
print(df['visit_concept_id'].value_counts().head(10))

# Calculate visit duration (in days)
df['visit_duration_days'] = (df['visit_end_datetime'] - df['visit_start_datetime']).dt.days

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. Distribution of visit types
ax1 = axes[0, 0]
visit_types = df['visit_concept_id'].value_counts().head(10)
visit_types.plot(kind='bar', ax=ax1)
ax1.set_title('Top 10 Visit Types Distribution')
ax1.set_xlabel('Visit Concept ID')
ax1.set_ylabel('Count')
ax1.tick_params(axis='x', rotation=45)

# 2. Visits over time (monthly)
ax2 = axes[0, 1]
df['visit_month'] = df['visit_start_datetime'].dt.to_period('M')
monthly_visits = df.groupby('visit_month').size()
monthly_visits.plot(ax=ax2)
ax2.set_title('Monthly Visit Trends')
ax2.set_xlabel('Month')
ax2.set_ylabel('Number of Visits')
ax2.tick_params(axis='x', rotation=45)

# 3. Visit duration distribution
ax3 = axes[1, 0]
duration_data = df['visit_duration_days'].dropna()
duration_data = duration_data[duration_data >= 0]  # Remove negative durations
duration_data[duration_data <= 30].hist(bins=30, ax=ax3)
ax3.set_title('Visit Duration Distribution (0-30 days)')
ax3.set_xlabel('Duration (days)')
ax3.set_ylabel('Frequency')

# 4. Visits per patient distribution
ax4 = axes[1, 1]
visits_per_patient = df.groupby('person_id').size()
visits_per_patient[visits_per_patient <= 20].hist(bins=20, ax=ax4)
ax4.set_title('Visits per Patient Distribution (1-20 visits)')
ax4.set_xlabel('Number of Visits')
ax4.set_ylabel('Number of Patients')

plt.tight_layout()
plt.savefig('visit_occurrence_eda.png', dpi=300, bbox_inches='tight')
plt.show()

# Additional analysis: Care site utilization
print("\n=== CARE SITE UTILIZATION ===")
care_site_visits = df.groupby('care_site_id').size().sort_values(ascending=False)
print("Top 10 most utilized care sites:")
print(care_site_visits.head(10))

# Summary statistics for visit duration
print("\n=== VISIT DURATION STATISTICS ===")
print(f"Average visit duration: {df['visit_duration_days'].mean():.2f} days")
print(f"Median visit duration: {df['visit_duration_days'].median():.2f} days")
print(f"Longest visit: {df['visit_duration_days'].max():.2f} days")

# Export summary report
with open('eda_summary_report.txt', 'w') as f:
    f.write("VISIT OCCURRENCE DATA - EDA SUMMARY REPORT\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
    f.write(f"Date Range: {df['visit_start_datetime'].min()} to {df['visit_start_datetime'].max()}\n")
    f.write(f"Unique Patients: {df['person_id'].nunique()}\n")
    f.write(f"Unique Visit Types: {df['visit_concept_id'].nunique()}\n")
    f.write(f"Unique Care Sites: {df['care_site_id'].nunique()}\n")
    f.write(f"Average Visits per Patient: {df.shape[0] / df['person_id'].nunique():.2f}\n")
    f.write(f"Average Visit Duration: {df['visit_duration_days'].mean():.2f} days\n")

print("\nEDA complete! Check 'visit_occurrence_eda.png' for visualizations")
print("and 'eda_summary_report.txt' for the summary report.")
