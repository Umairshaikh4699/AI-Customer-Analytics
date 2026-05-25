import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("AI Customer Analytics Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    # Load Data
    df = pd.read_csv(uploaded_file)

    # Show Dataset
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Dataset Information
    st.subheader("Dataset Shape")
    st.write(df.shape)

    # Column Names
    st.subheader("Columns")
    st.write(df.columns)

    # Missing Values
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Churn Distribution Graph
    if 'Churn' in df.columns:

        st.subheader("Churn Distribution")

        fig, ax = plt.subplots()

        sns.countplot(x='Churn', data=df, ax=ax)

        st.pyplot(fig)

    # Monthly Charges Histogram
    if 'MonthlyCharges' in df.columns:

        st.subheader("Monthly Charges Distribution")

        fig, ax = plt.subplots()

        sns.histplot(df['MonthlyCharges'], kde=True, ax=ax)

        st.pyplot(fig)

else:
    st.warning("Please upload a CSV file.")