# print("STARTING APP")
# from crews.fraud_crew import (
#     analyze_transaction
# )

# def main():
#     print("CALLING FRAUD AGENT")
#     transaction = """
#     Customer made ₹95,000 online
#     purchase at 2:30 AM
#     from Mumbai using a new device.
#     Average spending ₹4,000.
#     """

#     result = analyze_transaction(
#         transaction
#     )
#     print("RESULT RECEIVED")
#     print("\nRESULT:\n")
#     print(result)


# if __name__ == "__main__":
#     main()

print("APP STEP 1")

from crews.fraud_crew import (
    analyze_transaction
)

print("APP STEP 2")

from crews.credit_crew import (
    analyze_credit
)

print("APP STEP 3")


def main():

    print("\nSTARTING ANALYSIS\n")

    transaction = """
    Customer credit score 580.
    Income ₹45,000.
    Debt ratio 0.6.

    Customer made ₹95,000
    online transaction at 2 AM
    using a new device.

    Average spending ₹4,000.
    """

    print("RUNNING FRAUD AGENT\n")

    fraud_result = (
        analyze_transaction(
            transaction
        )
    )

    print("\nFRAUD RESULT\n")
    print("=" * 50)
    print(fraud_result)

    print("\nRUNNING CREDIT AGENT\n")

    credit_result = (
        analyze_credit(
            transaction
        )
    )

    print("\nCREDIT RESULT\n")
    print("=" * 50)
    print(credit_result)

    print("\nFINAL SUMMARY")
    print("=" * 50)

    print(
        f"Fraud Score: "
        f"{fraud_result['fraud_score']}"
    )

    print(
        f"Human Review: "
        f"{fraud_result['human_review']}"
    )

    print(
        f"Credit Status: "
        f"{credit_result['status']}"
    )


print("APP STEP 4")

if __name__ == "__main__":
    print("APP STEP 5")
    main()