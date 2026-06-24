# 📊 AI-Customer-Analytics

> An interactive churn prediction and customer retention dashboard — built to help businesses identify at-risk customers and act before it's too late.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Deployed on](https://img.shields.io/badge/Deployed%20on-Streamlit%20Cloud-FF4B4B?style=flat)

---

## 🚀 Overview

**AI-Customer-Analytics** is a data-driven churn prediction and retention intelligence dashboard. It ingests customer data, applies machine learning models to predict churn risk, and surfaces the insights through an interactive Streamlit interface — giving teams a clear picture of who's likely to leave and why.

The goal is simple: turn raw customer data into retention decisions. Instead of reacting to churn after it happens, this dashboard helps organizations identify at-risk customers early and take targeted action.

---

## ✨ Key Features

### 🔮 Churn Prediction
- ML model (Scikit-learn) trained on historical customer data
- Per-customer churn probability scores
- Risk segmentation: High / Medium / Low churn likelihood

### 📊 Retention Dashboard
- Real-time KPI cards: churn rate, retention rate, at-risk customer count
- Churn trend charts over time (monthly/quarterly)
- Revenue impact estimation from predicted churn

### 👥 Customer Segmentation
- Demographic breakdown of churned vs retained customers
- Segment-level churn rates by age, region, plan type, and tenure
- Heatmaps to surface high-risk customer clusters

### 📈 Visual Analytics
- Interactive charts built with Plotly and Seaborn
- Correlation analysis between features and churn outcome
- Exportable filtered data views for offline reporting

### 📂 Data Management
- CSV-based data ingestion — no database required
- Pandas-powered preprocessing and feature engineering
- Clean data pipeline from raw input to model-ready format

---

## 🛠️ Technology Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.8+ |
| **UI / App Framework** | Streamlit |
| **Data Processing** | Pandas, NumPy, SQL |
| **Machine Learning** | Scikit-learn |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Data Storage** | CSV / Local File Storage |
| **Notebooks** | Jupyter Notebook |
| **Development** | VS Code |
| **Version Control** | Git, GitHub |
| **Deployment** | Streamlit Cloud |

---

## ⚙️ Setup & Local Development

### Prerequisites

- Python 3.8 or higher
- pip
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/AI-Customer-Analytics.git
cd AI-Customer-Analytics

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run app.py
```

Opens at `http://localhost:8501` in your browser.

### Explore the Notebooks

```bash
jupyter notebook notebooks/
```

Use the EDA and model training notebooks to explore the dataset and retrain the churn model.

---

## 📂 Project Structure

```
AI-Customer-Analytics/
│
├── data/
│   └── Telco-Customer-Churn.csv
├── app.py                 
├── Analysis.py            
├── model.py               
├── segmentation.py        
├── style.css              
├── requirements.txt       
└── .gitignore             
```

---

## 🚀 Deployment

InterviewPulse is hosted on **Streamlit Cloud** with automatic redeployment on every push to `main`.

### Deploy Your Own Instance

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub and click **New app**
4. Select your fork → set `app.py` as the entry point
5. Click **Deploy**

Streamlit Cloud reads `requirements.txt` automatically — no additional config needed.

### Expected Dataset Format

Place your CSV at `data/customers.csv`. Minimum required columns:

| Column | Type | Description |
|---|---|---|
| `customer_id` | string | Unique customer identifier |
| `churn` | int (0/1) | Churn label — 1 = churned |
| `tenure` | int | Months as a customer |
| `monthly_charges` | float | Monthly billing amount |
| `contract_type` | string | Month-to-month / One-year / Two-year |

A sample dataset is included to get started immediately.

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add: your feature"`
4. Push and open a Pull Request

---


