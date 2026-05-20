from crewai import Task, Crew
from crews.fraud_crew import (
    analyze_transaction
)

from crews.credit_crew import (
    analyze_credit
)

from crews.audit_crew import (
    generate_audit
)


def run_full_analysis(
    transaction
):

    fraud_result = (
        analyze_transaction(
            transaction
        )
    )

    credit_result = (
        analyze_credit(
            transaction
        )
    )

    human_review = (
        fraud_result[
            "human_review"
        ]
    )

    audit_result = (
        generate_audit(
            fraud_result[
                "fraud_result"
            ],
            credit_result,
            human_review
        )
    )

    return {
        "fraud": fraud_result,
        "credit": credit_result,
        "audit": audit_result
    }