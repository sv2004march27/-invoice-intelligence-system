import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd

from invoice_intelligence_system.inference.predict_freight import predict_freight_cost
from invoice_intelligence_system.inference.predict_invoice_flag import predict_invoice_flag


# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📊",
    layout="wide"
)

# ===================== HEADER =====================
st.title("📊 Vendor Invoice Intelligence Portal")
st.markdown("""
### 🚀 AI-Driven Freight Cost Prediction & Invoice Risk Flagging

- 📦 Forecast freight costs accurately  
- 🚨 Detect risky or abnormal invoices  
- 💰 Reduce financial leakage  
""")

st.divider()

# ===================== SIDEBAR =====================
st.sidebar.title("⚙️ Model Selection")

selected_model = st.sidebar.radio(
    "Choose Prediction Module",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.markdown("""
### 📈 Business Impact
- Improved cost forecasting  
- Reduced invoice fraud  
- Faster finance operations  
""")

# =========================================================
# 🚚 FREIGHT COST PREDICTION
# =========================================================
if selected_model == "Freight Cost Prediction":

    st.subheader("🚚 Freight Cost Prediction")

    st.markdown("""
    **Objective:**  
    Predict freight cost using invoice dollars.
    """)

    with st.form("freight_form"):

        dollars = st.number_input(
            "💵 Invoice Dollars",
            min_value=1.0,
            value=18500.0
        )

        submit_freight = st.form_submit_button("🔮 Predict Freight Cost")

    if submit_freight:

        # ✅ ONLY required feature
        input_data = {
            "Dollars": [dollars]
        }

        result = predict_freight_cost(input_data)

        prediction = result["Predicted_Freight"].iloc[0]

        st.success("Prediction completed successfully 🎉")

        st.metric(
            label="📦 Estimated Freight Cost",
            value=f"${prediction:,.2f}"
        )


# =========================================================
# 🚨 INVOICE FLAG PREDICTION
# =========================================================
else:

    st.subheader("🚨 Invoice Manual Approval Prediction")

    st.markdown("""
    **Objective:**  
    Predict whether an invoice should be flagged for manual approval.
    """)

    with st.form("invoice_flag_form"):

        col1, col2, col3 = st.columns(3)

        with col1:
            invoice_quantity = st.number_input(
                "Invoice Quantity",
                min_value=1,
                value=50
            )

            freight = st.number_input(
                "Freight Cost",
                min_value=0.0,
                value=1.73
            )

        with col2:
            invoice_dollars = st.number_input(
                "Invoice Dollars",
                min_value=1.0,
                value=352.95
            )

            total_item_quantity = st.number_input(
                "Total Item Quantity",
                min_value=1,
                value=162
            )

        with col3:
            total_item_dollars = st.number_input(
                "Total Item Dollars",
                min_value=1.0,
                value=2476.0
            )

        submit_flag = st.form_submit_button("🧠 Evaluate Invoice Risk")

    if submit_flag:

        # ✅ EXACT features required by model
        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        result = predict_invoice_flag(input_data)

        flag = result["Predicted_Flag"].iloc[0]

        if flag == 1:
            st.error("🚨 Invoice requires MANUAL APPROVAL")
        else:
            st.success("✅ Invoice is SAFE for Auto-Approval")