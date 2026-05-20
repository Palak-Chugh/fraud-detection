import sys
import os
from dotenv import load_dotenv
load_dotenv()
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

# import streamlit as st
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

# import streamlit as st

# from crews.fraud_crew import (
#     analyze_transaction
# )
# from crews.credit_crew import (
#     analyze_credit
# )

# st.set_page_config(
#     page_title="Fraud AI"
# )

# st.title(
#     "AI Fraud Detection System"
# )

# transaction = st.text_area(
#     "Enter Transaction Details"
# )

# mode = st.selectbox(
#     "Select Analysis",
#     [
#         "Fraud",
#         "Credit"
#     ]
# )
# if mode == "Credit":

#     result = analyze_credit(
#         transaction
#     )

#     st.markdown(result)


# if st.button(
#     "Analyze Fraud"
# ):

#     with st.spinner(
#         "Analyzing..."
#     ):

#         result = (
#             analyze_transaction(
#                 transaction
#             )
#         )

#     st.subheader(
#         "Fraud Analysis"
#     )

#     st.markdown(
#         result[
#             "fraud_result"
#         ]
#     )

#     st.metric(
#         "Fraud Score",
#         result[
#             "fraud_score"
#         ]
#     )

#     if result[
#         "human_review"
#     ]:

#         st.error(
#             "Human Review Required"
#         )

#         decision = st.radio(
#             "Decision",
#             [
#                 "Approve",
#                 "Reject",
#                 "Need More Info"
#             ]
#         )

#         comment = st.text_area(
#             "Reviewer Comment"
#         )

#         if st.button(
#             "Submit Review"
#         ):

#             st.success(
#                 f"""
#                 Human Decision:
#                 {decision}
#                 """
#             )

#             st.write(
#                 comment
#             )

#     else:

#         st.success(
#             "Auto Approved"
#         )

import streamlit as st

from crews.master_crew import (
    run_full_analysis
)

from ui.dashboard_charts import (
    create_fraud_gauge,
    create_risk_chart
)

st.set_page_config(
    page_title="Agentic AI"
)

st.title(
    "Credit Risk & Fraud Detection"
)
st.info("""
### Example Prompt

Customer Credit Score: 580
Income: ₹45,000
Debt Ratio: 0.6
Loan History: Poor

Transaction:
₹95,000 online purchase
at 2:00 AM from Mumbai
using a new device.

Average spending ₹4,000.
""")

transaction = st.text_area(
    "Enter Transaction Data"
)

if st.button(
    "Analyze"
):

    with st.spinner(
        "Running Multi-Agent Analysis..."
    ):

        result = (
            run_full_analysis(
                transaction
            )
        )

    st.header(
        "Fraud Analysis"
    )

    st.markdown(
        result[
            "fraud"
        ]["fraud_result"]
    )

    st.metric(
        "Fraud Score",
        result[
            "fraud"
        ]["fraud_score"]
    )
    
    # IMPORTANT
    fraud_score = (
        result["fraud"]
        ["fraud_score"]
    )

    st.subheader(
        "Risk Dashboard"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(
            create_fraud_gauge(
                fraud_score
            ),
            use_container_width=True
        )

    with col2:

        st.plotly_chart(
            create_risk_chart(),
            use_container_width=True
        )

    st.divider()

    st.header(
        "Fraud Report"
    )

    st.markdown(
        result["fraud"]
        ["fraud_result"]
    )


    st.header(
        "Credit Analysis"
    )

    st.markdown(
        result[
            "credit"
        ]
    )

    st.header(
        "Audit Report"
    )

    st.markdown(
        result[
            "audit"
        ]
    )

    if result[
        "fraud"
    ][
        "human_review"
    ]:

        st.error(
            "Human Review Required"
        )

        decision = st.radio(
            "Decision",
            [
                "Approve",
                "Reject",
                "Need More Info"
            ]
        )

        comment = st.text_area(
            "Reviewer Comment"
        )

        if st.button(
            "Submit Decision"
        ):

            st.success(
                f"""
                Decision:
                {decision}
                """
            )

            st.write(
                comment
            )

    else:

        st.success(
            "Auto Approved"
        )