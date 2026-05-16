#pip install streamlit

"""
pip install -U \
streamlit \
langchain \
langchain-core \
langchain-community \
langchain-openai \
langchain-text-splitters \
faiss-cpu \
pypdf \
python-dotenv \
tiktoken
"""

# ==========================================================
# IMPORTS
# ==========================================================

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from orchestration.graph import run_pipeline
 
 # Load data
df = pd.read_csv("data/financials.csv")


# ==========================================================
# STREAMLIT CONFIG
# ==========================================================

st.set_page_config(
    page_title="Agentic Credit and Fraud Assistant",
    page_icon="💰",
    layout="wide",
)


st.title("Agentic Credit and Fraud Assitant")

st.markdown(
    """
Agentic Credit and Fraud Assitant:

- Retrieval-Augmented Generation (RAG)
- LangChain
- OpenAI GPT
- Financial Document Intelligence
"""
)
# Select company
company_id = st.selectbox(
    "Select Company",
    df["company_id"]
)


# Get company data
company_data = df[df["name"] == company_name].iloc[0].to_dict()


if st.button("Run Audit"):
    result = run_pipeline(company_data)
    
    quant_result = quant.analyze_company(company_id)

    research_result = research.read_report(
        f"data/audit_reports/{company_id}.pdf"
    )

    final_result = auditor.evaluate(
       quant_result,
        research_result
    )

    st.subheader("Quant Analysis")
    st.json(quant_result)

    st.subheader("Research Findings")
    st.json(research_result)

    st.subheader("Final Recommendation")
    st.json(final_result)
 

if st.button("Run AI Audit"):

    result = run_credit_audit(company_id)

    st.write(result)

    with st.expander("Agent Execution Trace"):

        st.write("Quant Agent → Completed")
        st.write("Research Agent → Completed")
        st.write("Fraud Agent → Completed")
        st.write("Auditor Agent → Finalized")