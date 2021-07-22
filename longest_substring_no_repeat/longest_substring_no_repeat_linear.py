class Solution:

    def _check_length(self, symb_pos_dct, symb, i_symb, s, max_len, lower_bound):
        if symb_pos_dct[symb] >= lower_bound:
           curr_len = i_symb - lower_bound
           lower_bound = symb_pos_dct[symb] + 1
           return max(max_len, curr_len), lower_bound

        return max_len, lower_bound

    def lengthOfLongestSubstring(self, s: str) -> int:
        symb_pos_dct = {}
        max_len = 0
        lower_bound = 0
        for i_symb, symb in enumerate(s):
            if symb in symb_pos_dct.keys():
                max_len, lower_bound = self._check_length(symb_pos_dct, symb, i_symb, s, max_len, lower_bound)
            symb_pos_dct[symb] = i_symb
        return max(max_len, (len(s) - lower_bound))


