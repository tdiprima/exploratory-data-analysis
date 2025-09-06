"""
Simple application
streamlit run app.py
"""

import pandas as pd
import streamlit as st

st.title("CSV Summary Report Generator")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")

        st.subheader("Data Preview")
        st.dataframe(df.head())

        st.subheader("Summary Report")

        st.markdown(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

        st.markdown("**Column Types:**")
        st.write(df.dtypes)

        st.markdown("**Missing Values per Column:**")
        st.write(df.isnull().sum())

        st.markdown("**Statistical Summary (Numerical Columns):**")
        st.write(df.describe())

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload a CSV file to get started.")
