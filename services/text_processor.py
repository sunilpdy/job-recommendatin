import re
from typing import List


class TextProcessor:

    STOP_WORDS = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "is",
        "are",
        "to",
        "of",
        "in",
        "for",
        "with",
        "on",
        "as",
        "at",
        "by",
        "from"
    }

    @staticmethod
    def clean_text(text: str) -> str:

        if not text:
            return ""

        text = text.lower()

        # Remove special characters
        text = re.sub(r"[^a-z0-9+#.\s]", " ", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @classmethod
    def tokenize(cls, text: str) -> List[str]:

        text = cls.clean_text(text)

        words = text.split()

        return [
            word
            for word in words
            if word not in cls.STOP_WORDS
        ]
