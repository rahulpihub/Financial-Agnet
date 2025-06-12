import streamlit as st
import requests

# Webhook URL
WEBHOOK_URL = "https://rahulpihub1.app.n8n.cloud/webhook/9e23b923-5a62-40e8-9cfb-066b028543cb"

# Streamlit page settings
st.set_page_config(page_title="Invoice Submission", page_icon="🧾", layout="centered")
st.title("🧾 Invoice Submission Form")

# Input fields
name = st.text_input("Name")
email = st.text_input("Email ID")
invoice_number = st.text_input("Invoice Number")

# Submit button
if st.button("Submit"):
    if not name or not email or not invoice_number:
        st.warning("Please fill in all fields before submitting.")
    else:
        payload = {
            "name": name,
            "email": email,
            "invoice_number": invoice_number
        }

        try:
            response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
            response.raise_for_status()
            st.success("✅ Data submitted successfully!")
            st.code(payload, language="json")
        except requests.exceptions.RequestException as e:
            st.error(f"⚠️ Failed to send data: {e}")

st.caption("Powered by Streamlit • © 2025")
