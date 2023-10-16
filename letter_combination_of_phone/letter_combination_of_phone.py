from typing import List


class Solution:

    def __init__(self):
        self.mapping_dct = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.res_combination = []

    def letterCombinations(self, digits: str) -> List[str]:

        if digits == '':
            return []

        if len(digits) == 1:
            return self.mapping_dct[digits[0]]

        self.res_combination = self.mapping_dct[digits[0]]
        digits = digits[1:]

        while len(digits):

            curr_combination_lst = []

            for saved_comb in self.res_combination:
                for input_comp in self.mapping_dct[digits[0]]:
                    curr_comb = ''.join([saved_comb, input_comp])
                    curr_combination_lst.append(curr_comb)

            self.res_combination = curr_combination_lst
            digits = digits[1:]

        return self.res_combination


