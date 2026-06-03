"""
AI Customer Analytics Platform
================================
Production-ready Streamlit dashboard for customer churn analysis,
segmentation, KPI tracking, and AI-driven business insights.
Developer: Your Name
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import io
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# PAGE CONFIGURATION
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Customer Analytics Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# GLOBAL STYLES
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.main { background: #0a0e1a; }
section[data-testid="stSidebar"] {
    background: #0d1117;
    border-right: 1px solid #1e2a3a;
}

/* ── Hero header ── */
.hero-header {
    background: linear-gradient(135deg, #0d1b2a 0%, #1a2744 50%, #0d1b2a 100%);
    border: 1px solid #1e3a5f;
    border-radius: 20px;
    padding: 40px 48px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(56,189,248,0.07) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    color: #e2f0ff;
    margin: 0 0 8px 0;
    letter-spacing: -0.5px;
}
.hero-subtitle {
    font-size: 1rem;
    color: #7ca7c8;
    margin: 0;
    font-weight: 300;
}
.hero-badge {
    display: inline-block;
    background: rgba(56,189,248,0.12);
    border: 1px solid rgba(56,189,248,0.3);
    color: #38bdf8;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 16px;
}

/* ── KPI cards ── */
.kpi-card {
    background: linear-gradient(145deg, #111827, #1a2233);
    border: 1px solid #1e3a5f;
    border-radius: 16px;
    padding: 24px;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
}
.kpi-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.4);
}
.kpi-card::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 16px 16px 0 0;
}
.kpi-card.blue::after   { background: linear-gradient(90deg, #38bdf8, #0ea5e9); }
.kpi-card.red::after    { background: linear-gradient(90deg, #f87171, #ef4444); }
.kpi-card.green::after  { background: linear-gradient(90deg, #34d399, #10b981); }
.kpi-card.amber::after  { background: linear-gradient(90deg, #fbbf24, #f59e0b); }
.kpi-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #4a6a8a;
    margin-bottom: 10px;
}
.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 2.1rem;
    font-weight: 700;
    color: #e2f0ff;
    margin-bottom: 6px;
}
.kpi-delta {
    font-size: 0.78rem;
    font-weight: 500;
    padding: 2px 8px;
    border-radius: 6px;
    display: inline-block;
}
.kpi-delta.up   { background: rgba(52,211,153,0.12); color: #34d399; }
.kpi-delta.down { background: rgba(248,113,113,0.12); color: #f87171; }
.kpi-icon { font-size: 1.8rem; float: right; margin-top: -4px; opacity: 0.7; }

/* ── Section titles ── */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #c9dfef;
    margin-bottom: 4px;
}
.section-subtitle {
    font-size: 0.82rem;
    color: #4a6a8a;
    margin-bottom: 20px;
}

/* ── Insight cards ── */
.insight-card {
    background: #111827;
    border: 1px solid #1e3a5f;
    border-left: 4px solid #38bdf8;
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 12px;
}
.insight-card.warn { border-left-color: #f87171; }
.insight-card.ok   { border-left-color: #34d399; }
.insight-card p { color: #9bb8cf; font-size: 0.9rem; margin: 0; }
.insight-card strong { color: #e2f0ff; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #0d1117;
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
    border-bottom: none !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    color: #4a6a8a;
    font-weight: 500;
    font-size: 0.88rem;
    padding: 8px 18px;
}
.stTabs [aria-selected="true"] {
    background: #1a2744 !important;
    color: #38bdf8 !important;
}

/* ── Sidebar nav ── */
.nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    border-radius: 10px;
    color: #7ca7c8;
    font-size: 0.88rem;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.15s;
    margin-bottom: 4px;
}
.nav-item:hover, .nav-item.active {
    background: #1a2744;
    color: #38bdf8;
}
.nav-icon { font-size: 1.1rem; width: 22px; text-align: center; }

/* ── Footer ── */
.footer {
    background: #0d1117;
    border: 1px solid #1e2a3a;
    border-radius: 14px;
    padding: 28px 32px;
    margin-top: 40px;
    text-align: center;
}
.footer h4 {
    font-family: 'Syne', sans-serif;
    color: #38bdf8;
    margin-bottom: 6px;
    font-size: 1.1rem;
}
.footer p { color: #4a6a8a; font-size: 0.82rem; margin: 0; }
.footer a { color: #38bdf8; text-decoration: none; margin: 0 8px; }
.footer a:hover { color: #7dd3fc; }

/* ── Upload area ── */
[data-testid="stFileUploader"] {
    background: #111827;
    border: 2px dashed #1e3a5f;
    border-radius: 14px;
    padding: 20px;
}

/* ── Plotly charts dark background ── */
.js-plotly-plot .plotly { background: transparent !important; }

/* ── Streamlit tweaks ── */
div[data-testid="stMetricValue"] { color: #38bdf8; font-family: 'Syne', sans-serif; }
.stAlert { border-radius: 10px; }
hr { border-color: #1e2a3a; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PLOTLY DARK THEME DEFAULTS
# ─────────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(17,24,39,0.6)",
    font=dict(family="DM Sans", color="#9bb8cf", size=12),
    title_font=dict(family="Syne", size=15, color="#c9dfef"),
    xaxis=dict(gridcolor="#1e2a3a", linecolor="#1e2a3a", zerolinecolor="#1e2a3a"),
    yaxis=dict(gridcolor="#1e2a3a", linecolor="#1e2a3a", zerolinecolor="#1e2a3a"),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#9bb8cf")),
    margin=dict(l=20, r=20, t=48, b=20),
    colorway=["#38bdf8","#34d399","#fbbf24","#f87171","#a78bfa","#fb923c","#f472b6"],
)
COLOR_CHURN = {"No": "#34d399", "Yes": "#f87171"}
COLOR_SEQ   = px.colors.sequential.Blues

# ─────────────────────────────────────────────
# HELPERS & CACHING
# ─────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def load_data(file) -> pd.DataFrame:
    """Load and clean uploaded CSV."""
    df = pd.read_csv(file)
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.dropna(subset=["TotalCharges"] if "TotalCharges" in df.columns else [], inplace=True)
    return df


@st.cache_data(show_spinner=False)
def run_kmeans(X_scaled: np.ndarray, n: int = 3):
    """Fit K-Means and return labels + inertia."""
    km = KMeans(n_clusters=n, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    return labels, km.inertia_


@st.cache_data(show_spinner=False)
def run_rf(X: pd.DataFrame, y: pd.Series):
    """Train a Random Forest and return model + feature importances."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    rf = RandomForestClassifier(n_estimators=150, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    report = classification_report(y_test, rf.predict(X_test), output_dict=True)
    importance = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=True)
    return importance, report


def kpi_card(label, value, delta, color, icon, delta_dir="up"):
    """Render a styled KPI card."""
    delta_class = "up" if delta_dir == "up" else "down"
    return f"""
    <div class="kpi-card {color}">
        <span class="kpi-icon">{icon}</span>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <span class="kpi-delta {delta_class}">{delta}</span>
    </div>"""


def insight_card(text, kind="info"):
    """Render an insight card."""
    cls = {"info": "", "warn": "warn", "ok": "ok"}.get(kind, "")
    return f'<div class="insight-card {cls}"><p>{text}</p></div>'


def section_header(title, subtitle=""):
    st.markdown(f'<div class="section-title">{title}</div>'
                f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def apply_plotly_theme(fig):
    fig.update_layout(**PLOTLY_LAYOUT)
    return fig


def to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:20px 0 24px 0">
        <div style="font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:800;color:#38bdf8;margin-bottom:4px">
            🧠 Analytics AI
        </div>
        <div style="font-size:0.75rem;color:#4a6a8a;letter-spacing:0.5px">Customer Intelligence Platform</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="nav-item active"><span class="nav-icon">📊</span> Dashboard</div>
    <div class="nav-item"><span class="nav-icon">👥</span> Segmentation</div>
    <div class="nav-item"><span class="nav-icon">🤖</span> ML Insights</div>
    <div class="nav-item"><span class="nav-icon">📥</span> Export</div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div style="font-size:0.78rem;color:#4a6a8a;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-bottom:12px">Filters</div>', unsafe_allow_html=True)

    # Filters are built dynamically after data is loaded (see below)
    filter_placeholder = st.empty()

    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.72rem;color:#2d4a62;text-align:center;padding:8px 0">
        v2.0 · Built with Streamlit & Plotly
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HERO HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <div class="hero-badge">✦ AI-POWERED PLATFORM</div>
    <div class="hero-title">Customer Analytics Dashboard</div>
    <div class="hero-subtitle">
        End-to-end churn intelligence · segmentation · predictive insights · retention optimization
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FILE UPLOAD
# ─────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "Upload your customer CSV dataset",
    type=["csv"],
    help="Supports Telco-style datasets with columns like Churn, tenure, MonthlyCharges, etc."
)

if uploaded_file is None:
    st.markdown("""
    <div style="text-align:center;padding:60px 0;color:#2d4a62">
        <div style="font-size:3rem;margin-bottom:16px">📂</div>
        <div style="font-family:'Syne',sans-serif;font-size:1.1rem;color:#4a6a8a">
            Upload a CSV to begin your analysis
        </div>
        <div style="font-size:0.82rem;color:#2d4a62;margin-top:8px">
            Supports Telco Churn, e-commerce, SaaS, and other customer datasets
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
with st.spinner("Processing dataset…"):
    df_raw = load_data(uploaded_file)

# ─────────────────────────────────────────────
# SIDEBAR FILTERS
# ─────────────────────────────────────────────
filter_cols = {
    "Gender":          "gender",
    "Contract Type":   "Contract",
    "Payment Method":  "PaymentMethod",
    "Internet Service":"InternetService",
    "Senior Citizen":  "SeniorCitizen",
}

active_filters = {}
with filter_placeholder.container():
    for label, col in filter_cols.items():
        if col in df_raw.columns:
            opts = sorted(df_raw[col].dropna().unique().tolist())
            sel = st.multiselect(label, opts, default=opts, key=f"flt_{col}")
            active_filters[col] = sel

# Apply filters
df = df_raw.copy()
for col, sel in active_filters.items():
    if col in df.columns and sel:
        df = df[df[col].isin(sel)]

if df.empty:
    st.warning("No data matches the selected filters. Adjust the sidebar filters.")
    st.stop()

# ─────────────────────────────────────────────
# COMPUTED METRICS
# ─────────────────────────────────────────────
total_customers = len(df)
has_churn  = "Churn" in df.columns
has_tenure = "tenure" in df.columns
has_mc     = "MonthlyCharges" in df.columns
has_tc     = "TotalCharges" in df.columns

churn_rate       = df["Churn"].value_counts(normalize=True).get("Yes", 0) * 100 if has_churn else 0
retention_rate   = 100 - churn_rate if has_churn else 0
avg_monthly      = df["MonthlyCharges"].mean() if has_mc else 0
avg_tenure       = df["tenure"].mean() if has_tenure else 0

# ─────────────────────────────────────────────
# KPI CARDS
# ─────────────────────────────────────────────
st.markdown('<div style="margin-bottom:8px"></div>', unsafe_allow_html=True)
section_header("📈 Key Performance Indicators", "Real-time snapshot of your customer base")

c1, c2, c3, c4 = st.columns(4)
c1.markdown(kpi_card("Total Customers",     f"{total_customers:,}",     "↑ 100% loaded",          "blue",  "👥",  "up"),   unsafe_allow_html=True)
c2.markdown(kpi_card("Churn Rate",           f"{churn_rate:.1f}%",       f"↓ {retention_rate:.1f}% retained", "red",   "📉",  "down"), unsafe_allow_html=True)
c3.markdown(kpi_card("Avg Monthly Charges",  f"${avg_monthly:,.2f}",     "Per active customer",    "amber", "💵",  "up"),   unsafe_allow_html=True)
c4.markdown(kpi_card("Retention Rate",       f"{retention_rate:.1f}%",   "Loyal customer share",   "green", "🔒",  "up"),   unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊  Churn Analysis",
    "📦  Distribution & Charges",
    "🎯  Segmentation",
    "🤖  ML & Prediction",
    "💡  AI Insights"
])

# ══════════════════════════════════════════════
# TAB 1 – CHURN ANALYSIS
# ══════════════════════════════════════════════
with tab1:
    section_header("Customer Churn Analysis", "Breakdown of churned vs retained customers")

    if not has_churn:
        st.info("No 'Churn' column found in this dataset.")
    else:
        col_a, col_b = st.columns(2)

        # Churn pie chart
        with col_a:
            churn_counts = df["Churn"].value_counts().reset_index()
            churn_counts.columns = ["Churn", "Count"]
            fig_pie = px.pie(
                churn_counts, names="Churn", values="Count",
                title="Churn Distribution",
                color="Churn", color_discrete_map=COLOR_CHURN,
                hole=0.55
            )
            fig_pie.update_traces(textposition="outside", textinfo="percent+label",
                                  marker=dict(line=dict(color="#0a0e1a", width=2)))
            apply_plotly_theme(fig_pie)
            st.plotly_chart(fig_pie, use_container_width=True)

        # Churn by Contract
        with col_b:
            if "Contract" in df.columns:
                cbc = df.groupby(["Contract", "Churn"]).size().reset_index(name="Count")
                fig_bar = px.bar(
                    cbc, x="Contract", y="Count", color="Churn",
                    title="Churn by Contract Type", barmode="group",
                    color_discrete_map=COLOR_CHURN
                )
                apply_plotly_theme(fig_bar)
                st.plotly_chart(fig_bar, use_container_width=True)
            else:
                st.info("No 'Contract' column available.")

        # Churn by tenure (binned)
        if has_tenure:
            df["Tenure Band"] = pd.cut(df["tenure"], bins=[0,12,24,36,48,60,100],
                                       labels=["0–12","12–24","24–36","36–48","48–60","60+"])
            tbc = df.groupby(["Tenure Band", "Churn"]).size().reset_index(name="Count")
            fig_tb = px.bar(
                tbc, x="Tenure Band", y="Count", color="Churn",
                title="Churn by Tenure Band", barmode="stack",
                color_discrete_map=COLOR_CHURN, text_auto=True
            )
            apply_plotly_theme(fig_tb)
            st.plotly_chart(fig_tb, use_container_width=True)

        # Churn by payment method
        if "PaymentMethod" in df.columns:
            pmc = df.groupby(["PaymentMethod", "Churn"]).size().reset_index(name="Count")
            fig_pm = px.bar(
                pmc, x="Count", y="PaymentMethod", color="Churn",
                orientation="h", title="Churn by Payment Method",
                color_discrete_map=COLOR_CHURN, barmode="stack"
            )
            apply_plotly_theme(fig_pm)
            st.plotly_chart(fig_pm, use_container_width=True)

# ══════════════════════════════════════════════
# TAB 2 – DISTRIBUTIONS & CHARGES
# ══════════════════════════════════════════════
with tab2:
    section_header("Distribution & Charges Analysis", "Revenue patterns and customer lifecycle")

    col_a, col_b = st.columns(2)

    with col_a:
        if has_mc:
            fig_mc = px.histogram(
                df, x="MonthlyCharges",
                color="Churn" if has_churn else None,
                color_discrete_map=COLOR_CHURN if has_churn else None,
                nbins=40, title="Monthly Charges Distribution",
                marginal="box", opacity=0.8
            )
            apply_plotly_theme(fig_mc)
            st.plotly_chart(fig_mc, use_container_width=True)

    with col_b:
        if has_tenure:
            fig_ten = px.histogram(
                df, x="tenure",
                color="Churn" if has_churn else None,
                color_discrete_map=COLOR_CHURN if has_churn else None,
                nbins=36, title="Tenure Distribution (months)",
                marginal="box", opacity=0.8
            )
            apply_plotly_theme(fig_ten)
            st.plotly_chart(fig_ten, use_container_width=True)

    # Scatter: tenure vs MonthlyCharges
    if has_mc and has_tenure:
        fig_sc = px.scatter(
            df, x="tenure", y="MonthlyCharges",
            color="Churn" if has_churn else None,
            color_discrete_map=COLOR_CHURN if has_churn else None,
            opacity=0.6, title="Tenure vs Monthly Charges",
            size_max=6,
            trendline="lowess"
        )
        apply_plotly_theme(fig_sc)
        st.plotly_chart(fig_sc, use_container_width=True)

    # Correlation heatmap
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(num_cols) >= 2:
        corr = df[num_cols].corr()
        fig_hm = go.Figure(go.Heatmap(
            z=corr.values,
            x=corr.columns.tolist(),
            y=corr.index.tolist(),
            colorscale="Blues",
            zmin=-1, zmax=1,
            text=corr.round(2).values,
            texttemplate="%{text}",
            hovertemplate="<b>%{y} × %{x}</b><br>r = %{z:.2f}<extra></extra>",
        ))
        fig_hm.update_layout(title="Correlation Heatmap", **PLOTLY_LAYOUT)
        st.plotly_chart(fig_hm, use_container_width=True)

# ══════════════════════════════════════════════
# TAB 3 – SEGMENTATION
# ══════════════════════════════════════════════
with tab3:
    section_header("Customer Segmentation", "K-Means clustering to group customers by behaviour")

    seg_features = [c for c in ["tenure", "MonthlyCharges", "TotalCharges"] if c in df.columns]

    if len(seg_features) < 2:
        st.info("Need at least 2 of: tenure, MonthlyCharges, TotalCharges for segmentation.")
    else:
        n_clusters = st.slider("Number of Segments", 2, 6, 3, key="seg_k")

        X_seg = df[seg_features].fillna(0)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_seg)

        labels, _ = run_kmeans(X_scaled, n_clusters)
        df_seg = df.copy()
        df_seg["Segment"] = [f"Segment {l+1}" for l in labels]

        col_a, col_b = st.columns(2)
        with col_a:
            x_ax = st.selectbox("X axis", seg_features, index=0, key="seg_x")
        with col_b:
            y_ax = st.selectbox("Y axis", seg_features, index=1, key="seg_y")

        fig_seg = px.scatter(
            df_seg, x=x_ax, y=y_ax,
            color="Segment", opacity=0.7,
            title=f"Customer Segments ({n_clusters} groups)",
            hover_data=["Segment"] + (["Churn"] if has_churn else [])
        )
        apply_plotly_theme(fig_seg)
        st.plotly_chart(fig_seg, use_container_width=True)

        # Segment summary table
        seg_summary = df_seg.groupby("Segment")[seg_features].mean().round(2)
        seg_summary["Count"] = df_seg["Segment"].value_counts().sort_index().values
        if has_churn:
            seg_summary["Churn %"] = (
                df_seg[df_seg["Churn"] == "Yes"].groupby("Segment").size() /
                df_seg.groupby("Segment").size() * 100
            ).round(1).values

        st.markdown("**Segment Summary**")
        st.dataframe(
            seg_summary.style.background_gradient(cmap="Blues", axis=0),
            use_container_width=True
        )

# ══════════════════════════════════════════════
# TAB 4 – ML & PREDICTION
# ══════════════════════════════════════════════
with tab4:
    section_header("Machine Learning & Churn Prediction", "Random Forest feature importance and model performance")

    if not has_churn:
        st.info("A 'Churn' column is required for predictive modelling.")
    else:
        ml_num = df.select_dtypes(include=[np.number]).columns.tolist()

        if len(ml_num) < 2:
            st.info("Not enough numeric columns for ML analysis.")
        else:
            y = (df["Churn"] == "Yes").astype(int)
            X_ml = df[ml_num].fillna(0)

            with st.spinner("Training model…"):
                importance, report = run_rf(X_ml, y)

            col_a, col_b = st.columns([2, 1])

            with col_a:
                fig_fi = go.Figure(go.Bar(
                    y=importance.index.tolist(),
                    x=importance.values.tolist(),
                    orientation="h",
                    marker=dict(
                        color=importance.values.tolist(),
                        colorscale="Blues",
                        line=dict(color="rgba(0,0,0,0)")
                    )
                ))
                fig_fi.update_layout(
                    title="Feature Importance (Random Forest)",
                    xaxis_title="Importance Score",
                    **PLOTLY_LAYOUT
                )
                st.plotly_chart(fig_fi, use_container_width=True)

            with col_b:
                st.markdown("**Model Performance**")
                acc = report.get("accuracy", 0)
                p1  = report.get("1", {}).get("precision", 0)
                r1  = report.get("1", {}).get("recall", 0)
                f1  = report.get("1", {}).get("f1-score", 0)

                for metric, value in [("Accuracy", acc), ("Precision (Churn)", p1),
                                      ("Recall (Churn)", r1), ("F1-Score (Churn)", f1)]:
                    st.metric(metric, f"{value:.2%}")

            # Confusion-style gauge
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=acc * 100,
                title={"text": "Model Accuracy", "font": {"color": "#c9dfef", "family": "Syne"}},
                delta={"reference": 80},
                gauge={
                    "axis": {"range": [0, 100], "tickcolor": "#4a6a8a"},
                    "bar": {"color": "#38bdf8"},
                    "bgcolor": "#1a2233",
                    "bordercolor": "#1e3a5f",
                    "steps": [
                        {"range": [0, 60],  "color": "#1a2233"},
                        {"range": [60, 80], "color": "#1e3a5f"},
                        {"range": [80, 100],"color": "#1a3655"},
                    ],
                    "threshold": {
                        "line": {"color": "#34d399", "width": 3},
                        "value": 80
                    }
                }
            ))
            fig_gauge.update_layout(paper_bgcolor="rgba(0,0,0,0)",
                                    font=dict(color="#9bb8cf"),
                                    height=260,
                                    margin=dict(t=30, b=0))
            st.plotly_chart(fig_gauge, use_container_width=True)

# ══════════════════════════════════════════════
# TAB 5 – AI INSIGHTS
# ══════════════════════════════════════════════
with tab5:
    section_header("💡 AI-Generated Business Insights", "Automated analysis of your customer data")

    insights = []

    if has_churn:
        if churn_rate > 30:
            insights.append(("warn",
                f"<strong>High Churn Alert:</strong> Your churn rate of <strong>{churn_rate:.1f}%</strong> "
                f"is critically high. Industry benchmark is ~15–20%. Immediate intervention is recommended."))
        elif churn_rate > 15:
            insights.append(("warn",
                f"<strong>Elevated Churn:</strong> Churn rate at <strong>{churn_rate:.1f}%</strong>. "
                f"Consider targeted retention campaigns for at-risk customers."))
        else:
            insights.append(("ok",
                f"<strong>Healthy Retention:</strong> Churn rate of <strong>{churn_rate:.1f}%</strong> "
                f"is within acceptable range. Focus on maintaining satisfaction."))

    if has_tenure and has_churn:
        churned_tenure = df[df["Churn"] == "Yes"]["tenure"].mean() if "Churn" in df.columns else None
        if churned_tenure and churned_tenure < 18:
            insights.append(("warn",
                f"<strong>Early Churn Pattern:</strong> Churned customers leave after an average of "
                f"<strong>{churned_tenure:.0f} months</strong>. Strengthen your onboarding for new customers."))

    if has_mc and has_churn:
        c_charges = df[df["Churn"] == "Yes"]["MonthlyCharges"].mean() if "Churn" in df.columns else None
        nc_charges = df[df["Churn"] == "No"]["MonthlyCharges"].mean() if "Churn" in df.columns else None
        if c_charges and nc_charges and c_charges > nc_charges:
            insights.append(("warn",
                f"<strong>Price Sensitivity:</strong> Churned customers paid on average "
                f"<strong>${c_charges:.2f}/mo</strong> vs ${nc_charges:.2f}/mo for retained ones. "
                f"Consider flexible pricing tiers."))

    if "Contract" in df.columns and has_churn:
        mc_churn = (df[df["Contract"] == "Month-to-month"]["Churn"] == "Yes").mean() * 100
        if mc_churn > 40:
            insights.append(("warn",
                f"<strong>Contract Risk:</strong> Month-to-month customers churn at "
                f"<strong>{mc_churn:.1f}%</strong>. Incentivise annual or two-year contracts."))

    if avg_monthly > 0:
        insights.append(("info",
            f"<strong>Revenue Baseline:</strong> Average monthly revenue per customer is "
            f"<strong>${avg_monthly:.2f}</strong>. Upsell opportunities exist in lower-tier customers."))

    if avg_tenure > 0:
        insights.append(("ok",
            f"<strong>Customer Lifecycle:</strong> Average customer tenure is "
            f"<strong>{avg_tenure:.0f} months</strong>. Long-term customers are your best advocates."))

    # Recommendations
    recommendations = [
        "🎯 <strong>Proactive Outreach</strong> — Contact customers within the first 90 days to build loyalty.",
        "💳 <strong>Incentivise Long-Term Contracts</strong> — Offer meaningful discounts for annual commitments.",
        "📱 <strong>Self-Service Portal</strong> — Reduce support friction with better digital tools.",
        "🏆 <strong>Loyalty Programme</strong> — Reward tenure milestones to reduce voluntary churn.",
        "📊 <strong>Predictive Alerts</strong> — Flag customers with high churn scores for early intervention.",
    ]

    col_a, col_b = st.columns([3, 2])

    with col_a:
        st.markdown("**Automated Insights**")
        for kind, text in insights:
            st.markdown(insight_card(text, kind), unsafe_allow_html=True)

    with col_b:
        st.markdown("**Retention Recommendations**")
        for r in recommendations:
            st.markdown(
                f'<div style="padding:12px 16px;margin-bottom:8px;background:#111827;'
                f'border-radius:10px;font-size:0.87rem;color:#9bb8cf;'
                f'border:1px solid #1e2a3a">{r}</div>',
                unsafe_allow_html=True
            )

# ─────────────────────────────────────────────
# DATASET PREVIEW & EXPORT
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📋  Dataset Preview (filtered)", expanded=False):
    st.dataframe(df.head(50), use_container_width=True)
    st.caption(f"Showing 50 of {len(df):,} rows · {len(df.columns)} columns")

col_dl1, col_dl2 = st.columns(2)
with col_dl1:
    st.download_button(
        label="📥  Download Filtered Dataset (CSV)",
        data=to_csv_bytes(df),
        file_name="filtered_customers.csv",
        mime="text/csv",
        use_container_width=True
    )

with col_dl2:
    summary = pd.DataFrame({
        "Metric": ["Total Customers", "Churn Rate (%)", "Retention Rate (%)",
                   "Avg Monthly Charges ($)", "Avg Tenure (months)"],
        "Value": [total_customers, f"{churn_rate:.2f}", f"{retention_rate:.2f}",
                  f"{avg_monthly:.2f}", f"{avg_tenure:.1f}"]
    })
    st.download_button(
        label="📊  Download Summary Report (CSV)",
        data=to_csv_bytes(summary),
        file_name="analytics_summary.csv",
        mime="text/csv",
        use_container_width=True
    )

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <h4>🧠 AI Customer Analytics Platform</h4>
    <p>Built with ❤️ using Python · Streamlit · Plotly · scikit-learn</p>
    <p style="margin-top:10px">
        <a href="https://github.com/" target="_blank">⭐ GitHub</a>
        <a href="https://linkedin.com/" target="_blank">🔗 LinkedIn</a>
        <a href="mailto:you@example.com">✉️ Contact</a>
    </p>
    <p style="margin-top:12px;font-size:0.72rem;color:#2d4a62">
        © 2025 · Portfolio Project · All Rights Reserved
    </p>
</div>
""", unsafe_allow_html=True)