from difflib import SequenceMatcher
from typing import List


class WordProcessor:

    def __init__(self, is_trim_used:bool=True, is_case_sensitiveness_checked:bool=False):
        self.__should_trim = is_trim_used
        self.__should_check_case = is_case_sensitiveness_checked

    def correct_command(self, word: str) -> str:
        word = word.strip() if self.__should_trim else word
        word = word.lower() if not self.__should_check_case else word
        return word

    @staticmethod
    def get_similar_word(command: str, list_of_words: List[str]) -> str:
        ratios = []
        for word in list_of_words:
            ratio = WordProcessor.__get_similarity_ratio(command, word)
            ratios.append(ratio)
        index_of_biggest_number = ratios.index(max(ratios))
        return list_of_words[index_of_biggest_number]

    @staticmethod
    def __get_similarity_ratio(first_word, second_word) -> float:
        return SequenceMatcher(None, first_word, second_word).ratio()
