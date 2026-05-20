from human_loop.thresholds import (
    FRAUD_THRESHOLD
)


class HumanReviewEngine:

    @staticmethod
    def needs_review(
        fraud_score
    ):

        return (
            fraud_score >
            FRAUD_THRESHOLD
        )