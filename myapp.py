import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# ── Page & Theme ───────────────────────────────────────────
st.set_page_config(
    page_title="Customer Churn Predictor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load model
model = load_model("customer_churn_ann.h5")

# Mapping dictionaries
binary_map       = {"Yes": 1, "No": 0}
gender_map       = {"Female": 1, "Male": 0}
internet_service = ['DSL', 'Fiber optic', 'No']
contract_types   = ['Month-to-month', 'One year', 'Two year']
payment_methods  = [
    'Bank transfer (automatic)',
    'Credit card (automatic)',
    'Electronic check',
    'Mailed check'
]

# ── Header ───────────────────────────────────────
st.markdown(
    """
    <div style="text-align:center; margin:20px 0;">
      <h1 style="color:#1F618D; font-weight:700;">
        🔍 Customer Churn Prediction App
      </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# ── About & How to Use ──────────────────────────────────────
st.markdown(
    """
    <div style="
        background-color:#EAF2F8;
        padding:20px;
        border-radius:10px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    ">
      <h4 style="color:#154360; font-weight:600;">About this app</h4>
      <p style="font-size:16px; color:#1B4F72;">
        This Customer Churn Prediction App uses a trained Artificial Neural Network (ANN) to predict whether a customer is likely to leave a service. 
        By entering customer details such as demographics, service usage, and billing information, the model estimates churn probability, helping businesses make informed decisions to improve customer retention.
      </p>
    </div>
    <div style="
      background-color:#FEF9E7;
      padding:20px;
      border-left: 5px solid #F1C40F;
      border-radius:8px;
      margin-bottom:20px;
      font-size:16px;
      color:#7D6608;
    ">
      <strong>🛠️ How to Use This App:</strong>
      <ul style="margin-top:10px; margin-left:20px;">
        <li>Fill in customer details in the form below.</li>
        <li>Click the <strong>“🎯 Predict Churn”</strong> button.</li>
        <li>See your recommendation immediately below the form.</li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# ── Input Form (split into two cols) ───────────────────────
st.header("📝 Enter Customer Details")
with st.form("input_form"):
    left, right = st.columns(2)

    with left:
        gender         = st.selectbox("👤 Gender", list(gender_map.keys()))
        senior         = st.radio("👵 Senior Citizen (Age ≥ 65 ?)", [0, 1], format_func=lambda x: "Yes" if x else "No")
        partner        = st.selectbox("💑 Partner (Has a Spouse or Partner ?)", list(binary_map.keys()))
        dependents     = st.selectbox("👶 Dependents (Children ?)", list(binary_map.keys()))
        phone          = st.selectbox("📞 Phone Service", list(binary_map.keys()))
        multiple_lines = st.selectbox("📱 Multiple Lines", ['No phone service', 'No', 'Yes'])
        st.markdown("---")
        contract_type  = st.selectbox("📜 Contract Type", contract_types)
        paperless      = st.checkbox("🧾 Paperless Billing", value=True)
        payment_method = st.selectbox("💳 Payment Method", payment_methods)

    with right:
        internet         = st.selectbox("🌐 Internet Service", internet_service)
        online_security  = st.selectbox("🛡 Online Security", ['No', 'Yes', 'No internet service'])
        online_backup    = st.selectbox("💾 Online Backup", ['No', 'Yes', 'No internet service'])
        device_prot      = st.selectbox("🔧 Device Protection", ['No', 'Yes', 'No internet service'])
        tech_support     = st.selectbox("🖥 Tech Support", ['No', 'Yes', 'No internet service'])
        streaming_tv     = st.selectbox("📺 Streaming TV", ['No', 'Yes', 'No internet service'])
        streaming_movies = st.selectbox("🎬 Streaming Movies", ['No', 'Yes', 'No internet service'])
        st.markdown("---")
        tenure           = st.slider("📅 Tenure (months)", 0, 72, 12)
        monthly_charges  = st.slider("💰 Monthly Charges (USD)", 0.0, 118.0, 60.0, 0.01)
    
    total_charges    = st.slider("💵 Total Charges (USD)", 0.0, 8684.0, 0.0, 0.01)
    submitted = st.form_submit_button("🎯 Predict Churn")

# ── Prediction Result (below the form) ────────────────────
if submitted:
    # Normalize numeric inputs
    t_scaled   = tenure / 72
    m_scaled   = monthly_charges / 118
    tot_scaled = total_charges / 8684

    # Build feature vector
    vec = [
        gender_map[gender],
        1 if senior == 1 else 0,
        binary_map[partner],
        binary_map[dependents],
        t_scaled,
        binary_map[phone],
        1 if multiple_lines == "Yes" else 0,
        1 if online_security == "Yes" else 0,
        1 if online_backup == "Yes" else 0,
        1 if device_prot == "Yes" else 0,
        1 if tech_support == "Yes" else 0,
        1 if streaming_tv == "Yes" else 0,
        1 if streaming_movies == "Yes" else 0,
        1 if paperless else 0,
        m_scaled,
        tot_scaled,
        *(1 if internet == svc else 0 for svc in internet_service),
        *(1 if contract_type == ct else 0 for ct in contract_types),
        *(1 if payment_method == pm else 0 for pm in payment_methods)
    ]

    # Compute churn probability
    probability    = model.predict(np.array([vec]))[0][0]
    RISK_THRESHOLD = 0.50
    high_risk      = probability >= RISK_THRESHOLD
    confidence     = probability if high_risk else 1 - probability
    border_color   = "#E74C3C" if high_risk else "#27AE60"
    stay_or_leave  = "leave" if high_risk else "stay"
    recommendation = (
        "Consider offering a retention incentive or support call."
        if high_risk
        else "No immediate action needed; keep up the great service!"
    )

    # Render in a single box with plain English
    st.markdown(
        f"""
        <div style="
            border: 4px solid {border_color};
            background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(0,0,0,0.05));
            padding: 25px;
            border-radius: 12px;
            text-align: left;
            box-shadow: 0 5px 10px rgba(0,0,0,0.1);
            margin-top: 20px;
        ">
          <h2 style="margin:0 0 10px 0; font-size:1.6rem; color:{border_color};">
            {"⚠️ High Risk of Churn" if high_risk else "✅ Low Risk of Churn"}
          </h2>
          <p style="font-size:1.2rem; color:#2C3E50; margin:0 0 10px 0;">
            There’s a <strong>{(probability if high_risk else 1 - probability):.2%}</strong> chance this customer will {stay_or_leave}.
          </p>
          <p style="font-size:1rem; color:#2C3E50; margin:0;">
            Recommendation: {recommendation}
          </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ── Project Details & Tech Stack ───────────────────────────
st.markdown(
    """
    <div style="
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        background-color:#EBF5FB;
        padding:20px;
        border-radius:8px;
        margin-top:30px;
        color:#1A5276;
    ">
      <div style="flex: 1 1 45%; min-width:200px; margin-bottom:10px;">
        <h4 style="margin-bottom:10px;">🔧 Tech Stack Used</h4>
        <ul style="margin:0; padding-left:20px; list-style-type:disc; font-size:14px;">
          <li>🐍 <strong>Python 3.9+</strong></li>
          <li>🖥️ <strong>Streamlit</strong> – Web Interface</li>
          <li>🤖 <strong>TensorFlow & Keras</strong> – ANN Modeling</li>
          <li>🧠 <strong>scikit-learn</strong> – Preprocessing & Evaluation</li>
          <li>📊 <strong>Pandas</strong> – Data Wrangling</li>
          <li>📈 <strong>Matplotlib</strong> – Visualizations</li>
          <li>📦 <strong>NumPy</strong> – Numerical Computing</li>
          <li>🚀 <strong>Streamlit Cloud / Docker</strong> – Deployment</li>
        </ul>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ── Footer ──────────────────────────────────────────────────
st.markdown(
    """
    <div style="text-align:center; color:#7F8C8D; margin:40px 0 20px; font-size:15px;">
      Built by <strong>Muhammed John</strong>, an aspiring Data Scientist and AI Engineer<br><br>
      <a href="https://maha-jr10.github.io/Johns-website/" target="_blank" style="margin: 0 12px;">
        <img src="https://img.icons8.com/fluency/48/domain.png" alt="Website" width="32" style="vertical-align:middle;">
      </a>
      <a href="https://github.com/maha-jr10" target="_blank" style="margin: 0 12px;">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="32" style="vertical-align:middle;">
      </a>
      <a href="https://www.linkedin.com/in/Maha-Jr" target="_blank" style="margin: 0 12px;">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="32" style="vertical-align:middle;">
      </a>
    </div>
    """,
    unsafe_allow_html=True
)