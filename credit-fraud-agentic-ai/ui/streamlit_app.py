import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

import streamlit as st
# from crews.test_crew import run_test_crew

# st.set_page_config(page_title="Agentic AI POC")

# st.title("Credit & Fraud Agentic AI")

# input_text = st.text_area(
#     "Enter transaction details"
# )

# if st.button("Analyze"):

#     with st.spinner("Analyzing..."):
#         result = run_test_crew(input_text)

#     st.success("Analysis Completed")

#     st.write(result)


from crews.fraud_crew import (
    analyze_transaction
)

st.set_page_config(
    page_title="Fraud AI POC"
)

st.title(
    "AI Fraud Detection System"
)

transaction = st.text_area(
    "Enter Transaction Details"
)

if st.button("Analyze Fraud"):

    with st.spinner(
        "Analyzing Transaction..."
    ):

        result = analyze_transaction(
            transaction
        )

    st.success("Completed")

    st.markdown(result)