import re

class Solution():
    #
    # def _get_quantifier(self):
    #     if self.i_pattern < len(self.pattern)-1:
    #         if self.pattern[self.i_pattern+1] == '*':
    #             self.i_pattern += 1
    #             return '*'
    #     return None
    #
    # def _get_next_pattern(self):
    #     if self.i_pattern < len(self.pattern)-1:
    #         return self.pattern[self.i_pattern+1]
    #     return None

    def cut_pattern(self, i_symb):
        if i_symb < len(self.pattern) - 1:
            self.pattern = self.pattern[i_symb + 1:]
        if i_symb == (len(self.pattern) - 1):
            self.pattern = ''

    def is_real_symbol(self, pattern):
        is_not_real_symbol = ('*' in pattern) | ('.' in pattern)
        return not is_not_real_symbol

    def _get_current_pattern(self):

        i_symb = 0
        pattern_lst, previous_pattern = [], ''
        has_string_patern_strarted = False

        while i_symb < len(self.pattern):
            curr_pattern = self.pattern[i_symb]

            if i_symb < len(self.pattern) - 1:
                if self.pattern[i_symb+1] == '*':
                    curr_pattern += '*'
                    i_symb += 1
                if curr_pattern == previous_pattern:
                    pattern_lst[-1][curr_pattern] += 1
                else:
                    pattern_lst.append({curr_pattern: 1})

            if self.is_real_symbol(curr_pattern):
                if not has_string_patern_strarted:
                    has_string_patern_strarted = True
            else:
                if has_string_patern_strarted:
                    strin_pattern_final_symb = i_symb-len(curr_pattern)
                    self.cut_pattern(strin_pattern_final_symb)
                    pattern_lst = pattern_lst[:-1]
                    return pattern_lst

            if i_symb == (len(self.pattern) - 1):
                self.pattern = ''
                return pattern_lst

            i_symb += 1
            previous_pattern = curr_pattern

        return pattern_lst

    def _get_letters_only(self, pattern_lst):
        letters_only = ''
        for i_dct in range(1, len(pattern_lst)+1):
            curr_dct = pattern_lst[-i_dct]
            k, v = list(curr_dct.items())[0]
            if self.is_real_symbol(k):
                letters_only = k * v + letters_only
            else:
                return letters_only


    def reduce_string(self, substring):
        string_lst, previous_str = [], ''

        for i_symb in range(len(substring)):
            curr_str = substring[i_symb]

            if curr_str == previous_str:
                string_lst[-1][curr_str] += 1
            else:
                string_lst.append({curr_str: 1})

        return string_lst

    def isMatch(self, input_str, pattern):
        self.pattern = pattern
        self.input_str = input_str
        print(input_str)

        while len(self.pattern) > 0:
            curr_pattern_lst = self._get_current_pattern()
            print(curr_pattern_lst)
            letters_only_string = self._get_letters_only(curr_pattern_lst)

            if len(letters_only_string):
                has_pattern_found = re.search(letters_only_string, self.input_str)
                if has_pattern_found:
                    final_position = has_pattern_found.span()[1]
                    string_to_digest = self.input_str[:final_position]
                    curr_string_lst = self.reduce_string(string_to_digest)
                    print('string list-->', curr_string_lst)

                    for pattern_dct in reversed(curr_pattern_lst):
                        k_pattern, v_pattern = list(pattern_dct.items())[0]
                        if self.is_real_symbol(k_pattern):
                            while len(curr_string_lst):
                                k_string, v_string = list(curr_string_lst[-1].items())[0]

                                if k_pattern != k_string:
                                    return False

                                curr_string_lst[-1][k_pattern] -= v_pattern
                                if curr_string_lst[-1][k_pattern] == 0:
                                    curr_pattern_lst.pop(-1)


u = Solution()
u.isMatch('abbaa', 'a*.aba*bb*b*')


