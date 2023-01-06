from src import Normalizer, Levenshtein

class FileComparer:
    def __init__(self, normalizer: Normalizer, distance_calculator: Levenshtein):
        self.normalizer = normalizer
        self.distance_calculator = distance_calculator

    def compare(self, file1: str, file2: str) -> float:
        """
        Calculate the similarity of two files by comparing their contents.
        """
        with open(file1, 'r', encoding="utf8") as f1, open(file2, 'r', encoding="utf8") as f2:
            text1 = f1.read()
            text2 = f2.read()
            text1 = self.normalizer.normalize(text1)
            text2 = self.normalizer.normalize(text2)
            return 1 - self.distance_calculator.distance(text1, text2) / max(len(text1), len(text2))