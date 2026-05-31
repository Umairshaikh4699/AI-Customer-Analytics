import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(
    page_title="AI Customer Analytics",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1 {
    color: #4CAF50;
    text-align: center;
}

.stMetric {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<h1>📊 AI Customer Analytics Dashboard</h1>
""", unsafe_allow_html=True)

st.write("---")

# Sidebar
st.sidebar.header("📁 Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# Main App
if uploaded_file is not None:

    # Load Data
    df = pd.read_csv(uploaded_file)

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    # Dataset Preview
    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head(), use_container_width=True)

    st.write("---")

    # KPI Cards
    st.subheader("📌 Dashboard KPIs")

    col1, col2, col3 = st.columns(3)

    total_customers = len(df)

    if 'MonthlyCharges' in df.columns:
        total_revenue = round(df['MonthlyCharges'].sum(), 2)
    else:
        total_revenue = 0

    if 'Churn' in df.columns:
        churn_rate = round(
            (df['Churn'].value_counts(normalize=True).get('Yes', 0)) * 100,
            2
        )
    else:
        churn_rate = 0

    col1.metric("👥 Total Customers", total_customers)
    col2.metric("💰 Total Revenue", f"₹ {total_revenue}")
    col3.metric("📉 Churn Rate", f"{churn_rate}%")

    st.write("---")

    # Dataset Information
    st.subheader("📊 Dataset Information")

    info_col1, info_col2 = st.columns(2)

    with info_col1:
        st.write("### Shape")
        st.write(df.shape)

        st.write("### Columns")
        st.write(list(df.columns))

    with info_col2:
        st.write("### Missing Values")
        st.write(df.isnull().sum())

    st.write("---")

    # Graphs Section
    st.subheader("📈 Customer Analytics Charts")

    chart_col1, chart_col2 = st.columns(2)

    # Churn Distribution
    if 'Churn' in df.columns:

        with chart_col1:

            st.write("### Churn Distribution")

            fig, ax = plt.subplots(figsize=(5,4))

            sns.countplot(
                x='Churn',
                data=df,
                palette='Set2',
                ax=ax
            )

            st.pyplot(fig)

    # Monthly Charges Histogram
    if 'MonthlyCharges' in df.columns:

        with chart_col2:

            st.write("### Monthly Charges Distribution")

            fig, ax = plt.subplots(figsize=(5,4))

            sns.histplot(
                df['MonthlyCharges'],
                kde=True,
                color='skyblue',
                ax=ax
            )

            st.pyplot(fig)

    st.write("---")

    # Correlation Heatmap
    st.subheader("🔥 Correlation Heatmap")

    numeric_df = df.select_dtypes(include=['number'])

    if not numeric_df.empty:

        fig, ax = plt.subplots(figsize=(10,6))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap='coolwarm',
            ax=ax
        )

        st.pyplot(fig)

    st.write("---")

    # Full Dataset
    with st.expander("🔍 View Full Dataset"):

        st.dataframe(df, use_container_width=True)

else:

    st.info("⬅️ Upload a CSV file from the sidebar to start analytics")