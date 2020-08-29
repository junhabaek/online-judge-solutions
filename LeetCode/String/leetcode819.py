import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        pure_words = re.sub('[^a-z\s]', ' ', paragraph).split()

        word_counts = {}
        for word in pure_words:
            if word not in banned:
                word_counts[word] = word_counts.get(word, 0) + 1

        max_word = max(word_counts.keys(), key=lambda cur_word: word_counts[cur_word])
        # max_word = max(word_counts.keys(), key = word_counts.get)

        return max_word