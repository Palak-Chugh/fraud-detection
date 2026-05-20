import json
from pathlib import Path


class AdaptiveMemory:

    def __init__(self):

        self.memory_file = Path(
            "memory/history.json"
        )

        self.memory_file.parent.mkdir(
            exist_ok=True
        )

        if not self.memory_file.exists():

            self.memory_file.write_text(
                "[]",
                encoding="utf-8"
            )

    def store_case(
        self,
        transaction,
        result
    ):

        history = self._load()

        history.append({
            "transaction":
            transaction,

            "result":
            result
        })

        self.memory_file.write_text(
            json.dumps(
                history,
                indent=2
            ),
            encoding="utf-8"
        )

    def retrieve_similar_cases(
        self,
        transaction,
        limit=3
    ):

        history = self._load()

        transaction_words = set(
            transaction.lower().split()
        )

        scored = []

        for item in history:

            previous_text = (
                item["transaction"]
                .lower()
            )

            similarity = len(
                transaction_words.intersection(
                    previous_text.split()
                )
            )

            scored.append(
                (
                    similarity,
                    item
                )
            )

        scored.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        return [
            item["result"]
            for _, item in scored[:limit]
        ]

    def _load(self):

        return json.loads(
            self.memory_file.read_text(
                encoding="utf-8"
            )
        )