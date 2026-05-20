from crews.fraud_crew import (
    analyze_transaction
)


class FraudService:

    @staticmethod
    def run_fraud_analysis(
        transaction
    ):

        if not transaction:

            return {
                "status":
                "error",

                "message":
                "Transaction input required"
            }

        try:

            result = (
                analyze_transaction(
                    transaction
                )
            )

            return {
                "status":
                "success",

                "data":
                result
            }

        except Exception as e:

            return {
                "status":
                "error",

                "message":
                str(e)
            }