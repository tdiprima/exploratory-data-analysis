# streamlit run fixed_streamlit_app.py
import pandas as pd
import streamlit as st

st.title("CSV Summary Report Generator")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Fix data types to make Arrow-compatible
        for col in df.columns:
            if df[col].dtype == "object":
                # Convert object columns to string type
                df[col] = df[col].astype("string")

        st.success("File uploaded successfully!")

        st.subheader("Data Preview")
        st.dataframe(df.head())

        st.subheader("Summary Report")

        st.markdown(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

        st.markdown("**Column Types:**")

        # Create a clean display of column types
        col_types = pd.DataFrame(
            {"Column": df.columns, "Type": [str(dtype) for dtype in df.dtypes]}
        )
        st.dataframe(col_types, hide_index=True)

        st.markdown("**Missing Values per Column:**")
        missing_data = pd.DataFrame(
            {
                "Column": df.columns,
                "Missing Count": df.isnull().sum().values,
                "Missing %": (df.isnull().sum() / len(df) * 100).round(2).values,
            }
        )
        st.dataframe(missing_data, hide_index=True)

        # Only show statistical summary if there are numerical columns
        numeric_cols = df.select_dtypes(include=["number"]).columns
        if len(numeric_cols) > 0:
            st.markdown("**Statistical Summary (Numerical Columns):**")
            st.dataframe(df[numeric_cols].describe())
        else:
            st.markdown(
                "**Statistical Summary:** No numerical columns found in the dataset."
            )

        # Additional insights
        st.subheader("Additional Insights")

        # Show unique values for categorical columns
        categorical_cols = df.select_dtypes(include=["string", "object"]).columns
        if len(categorical_cols) > 0:
            st.markdown("**Unique Values in Categorical Columns:**")
            for col in categorical_cols[:5]:  # Show first 5 categorical columns
                unique_count = df[col].nunique()
                st.write(f"**{col}:** {unique_count} unique values")
                if unique_count <= 10:  # Show values if not too many
                    st.write(f"Values: {', '.join(map(str, df[col].unique()))}")

    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.write("Please make sure your CSV file is properly formatted.")
else:
    st.info("Please upload a CSV file to get started.")
