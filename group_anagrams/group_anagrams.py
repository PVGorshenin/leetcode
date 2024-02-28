from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, input_words: List[str]) -> List[List[str]]:
        res_lst = []

        word_dct = defaultdict(list)

        for word in input_words:

            sorted_word = ''.join(sorted(word))

            word_dct[sorted_word].append(word)

        for _, annagram_lst in word_dct.items():
            res_lst.append(list(annagram_lst))

        return res_lst
