import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


# Title
st.title("AI Customer Analytics Dashboard")


# Upload CSV
uploaded_file = st.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)


if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.write(df.head())


    # KPIs
    st.subheader("Key Metrics")

    total_customers = len(df)

    st.write("Total Customers:", total_customers)


    churn_rate = df['Churn'].value_counts(normalize=True) * 100

    st.write(churn_rate)


    # Churn Graph
    st.subheader("Customer Churn Graph")

    fig, ax = plt.subplots()

    df['Churn'].value_counts().plot(
        kind='bar',
        ax=ax
    )

    st.pyplot(fig)


    # Segmentation
    st.subheader("Customer Segmentation")

    X = df[['Age', 'MonthlyCharges', 'Tenure']]

    kmeans = KMeans(n_clusters=3)

    kmeans.fit(X)

    df['Cluster'] = kmeans.labels_


    # Segmentation Graph
    fig2, ax2 = plt.subplots()

    ax2.scatter(
        df['MonthlyCharges'],
        df['Tenure'],
        c=df['Cluster']
    )

    ax2.set_xlabel("Monthly Charges")
    ax2.set_ylabel("Tenure")

    st.pyplot(fig2)


    # Prediction Button
    st.subheader("Prediction")

    if st.button("Predict Churn"):

        st.success("Prediction Completed")