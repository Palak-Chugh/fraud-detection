import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

# import streamlit as st
# # from crews.test_crew import run_test_crew

# # st.set_page_config(page_title="Agentic AI POC")

# # st.title("Credit & Fraud Agentic AI")

# # input_text = st.text_area(
# #     "Enter transaction details"
# # )

# # if st.button("Analyze"):

# #     with st.spinner("Analyzing..."):
# #         result = run_test_crew(input_text)

# #     st.success("Analysis Completed")

# #     st.write(result)

# import streamlit as st

# from crews.fraud_crew import (
#     analyze_transaction
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

st.set_page_config(
    page_title="Agentic AI"
)

st.title(
    "Credit Risk & Fraud Detection"
)

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