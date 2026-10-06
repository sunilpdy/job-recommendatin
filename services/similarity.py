from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:

    def __init__(self):

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            sublinear_tf=True
        )

    def calculate_similarity(
        self,
        candidate_text: str,
        job_texts: List[str]
    ) -> List[float]:

        documents = [candidate_text] + job_texts

        matrix = self.vectorizer.fit_transform(
            documents
        )

        candidate_vector = matrix[0]

        job_vectors = matrix[1:]

        similarities = cosine_similarity(
            candidate_vector,
            job_vectors
        )[0]

        return [
            round(float(score) * 100, 2)
            for score in similarities
        ]
