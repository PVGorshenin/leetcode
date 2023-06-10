import re

import numpy as np

class Solution():


    def is_real_symbol(self, pattern):
        is_not_real_symbol = ('*' in pattern) | ('.' in pattern)
        return not is_not_real_symbol and len(pattern)

    def _reduce_pattern(self):

        i_symb = 0
        pattern_lst, previous_pattern = [], ''

        while i_symb < len(self.pattern):
            curr_pattern = self.pattern[i_symb]

            if i_symb < len(self.pattern) - 1:
                if self.pattern[i_symb+1] == '*':
                    curr_pattern += '*'
                    i_symb += 1

            if (curr_pattern == previous_pattern) and (not self.is_real_symbol(curr_pattern)):
                pass
            elif self.is_real_symbol(curr_pattern) and self.is_real_symbol(previous_pattern):
                pattern_lst[-1] += curr_pattern
            elif curr_pattern == '.' and previous_pattern == '.':
                pattern_lst[-1] += curr_pattern
            else:
                pattern_lst.append(curr_pattern)

            i_symb += 1
            previous_pattern = curr_pattern

        return pattern_lst

    def fillup_matrix(self):
        for i_row, pattern in enumerate(self.reduced_pattern_lst):
            pattern = pattern.replace('*', '')

            if self.is_real_symbol(pattern):
                for match in re.finditer(pattern, self.input_str):
                    self.match_matrix[i_row, match.span()[0]:match.span()[1]] = 1
            if '.' in pattern:
                self.match_matrix[i_row] = 1

    def get_priority(self, pattern_lst):
        priority_lst = []
        median = len(pattern_lst) // 2
        for i_from_border in range(median):
            last_now = self.reduced_pattern_lst[-(i_from_border+1)]
            first_now = self.reduced_pattern_lst[i_from_border]

            if self.is_real_symbol(last_now) or last_now == '.':
                priority_lst.append(len(pattern_lst) - i_from_border - 1)

            if self.is_real_symbol(first_now) or first_now == '.':
                priority_lst.append(i_from_border)

        if len(pattern_lst) % 2:
            median_el = self.reduced_pattern_lst[median]
            if self.is_real_symbol(median_el) or median_el == '.':
                priority_lst.append(median)

        for i_from_border in range(median):
            last_now = self.reduced_pattern_lst[-(i_from_border + 1)]
            first_now = self.reduced_pattern_lst[i_from_border]

            if '*' in last_now:
                priority_lst.append(len(pattern_lst) - i_from_border - 1)

            if '*' in first_now:
                priority_lst.append(i_from_border)

        if median not in priority_lst:
            priority_lst.append(median)

        return priority_lst

    def add_zeros_to_matrix(self, i_row, i_col, len_of_pattern):
        self.match_matrix[:i_row, i_col:] = 0
        self.match_matrix[i_row:, :i_col + len_of_pattern] = 0
        self.match_matrix[i_row] = 0
        self.match_matrix[i_row, i_col: i_col + len_of_pattern] = 1

    def decision(self):
        median = self.match_matrix.shape[0] // 2
        for i_priority, curr_row in enumerate(self.priority_lst):
            curr_pattern = self.reduced_pattern_lst[curr_row]
            has_match_found = False
            print(curr_pattern)

            if '*' in curr_pattern:
                if curr_row >= median:
                    for i_col in range(self.match_matrix.shape[1]-1, 0, -1):
                        if self.match_matrix[curr_row, i_col] == 1:
                            finish_col = i_col
                            while (self.match_matrix[curr_row, i_col] == 1) and (i_col >= 0):
                                start_col = i_col
                                i_col -= 1
                    len_of_ones = finish_col - start_col

                    self.add_zeros_to_matrix(curr_row, start_col, len_of_ones)


            if curr_row >= median:
                for i_col in range(self.match_matrix.shape[1], 0, -1):
                    if self.match_matrix[curr_row, i_col:i_col + len(curr_pattern)].sum() == len(curr_pattern):
                        has_match_found = True
                        self.add_zeros_to_matrix(curr_row, i_col, len(curr_pattern))

            if curr_row < median:
                for i_col in range(self.match_matrix.shape[1]):

                    if self.match_matrix[curr_row, i_col: i_col + len(curr_pattern)].sum() == len(curr_pattern):
                        has_match_found = True
                        self.add_zeros_to_matrix(curr_row, i_col, len(curr_pattern))

                        # print(curr_pattern, i_col, curr_row)
                        # print(self.match_matrix)
            if not has_match_found:
                return False


    def isMatch(self, input_str, pattern):
        self.pattern = pattern
        self.input_str = input_str

        self.reduced_pattern_lst = self._reduce_pattern()

        self.match_matrix = np.zeros((len(self.reduced_pattern_lst), len(self.input_str)))

        self.fillup_matrix()
        print(self.match_matrix)

        self.priority_lst = self.get_priority(self.reduced_pattern_lst)

        self.decision()
        print()
        print('input --> ', self.input_str)
        print('pattern -->', self.pattern)
        print('priority --> ', self.priority_lst)
        print('reduced pattern', self.reduced_pattern_lst)
        print(self.match_matrix)
        print(self.match_matrix.sum(0).sum() == len(self.input_str))
        return self.match_matrix.sum(0).sum() == len(self.input_str)


u = Solution()
u.isMatch('mississippi', 'mis*is*ip*.')


