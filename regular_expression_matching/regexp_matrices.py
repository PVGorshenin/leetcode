import re

import numpy as np

class Solution():


    def is_real_symbol(self, pattern):
        is_not_real_symbol = ('*' in pattern)
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

            if (curr_pattern == previous_pattern) and '*' in curr_pattern:
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
            re_pattern = re.compile(r'(?=({}))'.format(pattern))

            if self.is_real_symbol(pattern):
                for match in re.finditer(re_pattern, self.input_str):
                    self.match_matrix[i_row, match.start(1):match.end(1)] = 1

    def get_priority(self, pattern_lst):
        priority_lst = []
        median = len(pattern_lst) // 2

        for i_from_border in range(median):
            last_now = self.reduced_pattern_lst[-(i_from_border+1)]
            first_now = self.reduced_pattern_lst[i_from_border]

            if self.is_real_symbol(last_now):
                priority_lst.append(len(pattern_lst) - i_from_border - 1)

            if self.is_real_symbol(first_now):
                priority_lst.append(i_from_border)

        if len(pattern_lst) % 2:
            median_el = self.reduced_pattern_lst[median]
            if self.is_real_symbol(median_el):
                priority_lst.append(median)

        for i_from_border in range(median):
            last_now = self.reduced_pattern_lst[-(i_from_border + 1)]
            first_now = self.reduced_pattern_lst[i_from_border]

            if '.*' in last_now:
                priority_lst.append(len(pattern_lst) - i_from_border - 1)

            if '.*' in first_now:
                priority_lst.append(i_from_border)

        if len(pattern_lst) % 2:
            median_el = self.reduced_pattern_lst[median]
            if '.*' in median_el:
                priority_lst.append(median)

        for i_from_border in range(median):
            last_now = self.reduced_pattern_lst[-(i_from_border + 1)]
            first_now = self.reduced_pattern_lst[i_from_border]

            if ('*' in last_now) and ('.*' not in last_now):
                priority_lst.append(len(pattern_lst) - i_from_border - 1)

            if '*' in first_now and ('.*' not in first_now):
                priority_lst.append(i_from_border)

        if median not in priority_lst:
            priority_lst.append(median)

        return priority_lst

    def add_zeros_to_matrix(self, i_row, i_col, len_of_pattern):
        self.match_matrix[:i_row, i_col:] = 0
        self.match_matrix[i_row:, :i_col + len_of_pattern] = 0
        self.match_matrix[i_row] = 0
        self.match_matrix[i_row, i_col: i_col + len_of_pattern] = 1

    def decision(self, pattern_to_turn=None, pattern_to_move=None, starting_point=0):

        basic_starting_point = starting_point
        median = self.match_matrix.shape[0] // 2
        for i_priority, curr_row in enumerate(self.priority_lst):

            curr_pattern = self.reduced_pattern_lst[curr_row]
            has_match_found = False

            if '*' not in curr_pattern:

                is_more_then_median = curr_row >= median

                if curr_row == pattern_to_turn:
                    is_more_then_median = not is_more_then_median

                if curr_row != pattern_to_move:
                    starting_point = 0
                else:
                    starting_point = basic_starting_point


                if is_more_then_median:

                    for i_col in range(self.match_matrix.shape[1]-1-starting_point, -1, -1):
                        if self.match_matrix[curr_row, i_col:i_col + len(curr_pattern)].sum() == len(curr_pattern):
                            has_match_found = True
                            self.add_zeros_to_matrix(curr_row, i_col, len(curr_pattern))



                else:


                    for i_col in range(starting_point, self.match_matrix.shape[1]):
                        if self.match_matrix[curr_row, i_col: i_col + len(curr_pattern)].sum() == len(curr_pattern):

                            has_match_found = True
                            self.add_zeros_to_matrix(curr_row, i_col, len(curr_pattern))

                if not has_match_found:
                    return False

            else:

                if curr_row >= median:
                    for i_col in range(self.match_matrix.shape[1]-1, -1, -1):
                        if self.match_matrix[curr_row, i_col] == 1:
                            finish_col = i_col

                            while (i_col >= 0) and (self.match_matrix[curr_row, i_col] == 1):
                                start_col = i_col
                                i_col -= 1

                            len_of_ones = finish_col - start_col + 1
                            self.add_zeros_to_matrix(curr_row, start_col, len_of_ones)
                            break

                else:
                    for i_col in range(0, self.match_matrix.shape[1]):
                        if self.match_matrix[curr_row, i_col] == 1:
                            start_col = i_col

                            while (i_col < self.match_matrix.shape[1]) and (self.match_matrix[curr_row, i_col] == 1):
                                finish_col = i_col
                                i_col += 1

                            len_of_ones = finish_col - start_col + 1
                            self.add_zeros_to_matrix(curr_row, start_col, len_of_ones)
                            break

        return True

    def _here_we_go_again(self, input_str, pattern, pattern_to_turn=None, pattern_to_move=None, starting_point=0):


        self.pattern = pattern
        self.input_str = input_str
        self.reduced_pattern_lst = self._reduce_pattern()
        self.match_matrix = np.zeros((len(self.reduced_pattern_lst), len(self.input_str)))
        self.fillup_matrix()
        self.priority_lst = self.get_priority(self.reduced_pattern_lst)


        _ = self.decision(
            pattern_to_turn=pattern_to_turn,
            pattern_to_move=pattern_to_move,
            starting_point=starting_point)

        is_match = self.match_matrix.sum(0).sum() == len(self.input_str)
        is_rows_ones = self.match_matrix.sum(0).max() == 1

        is_match &= is_rows_ones
        return is_match

    def aux_print(self, is_match):
        print('input --> ', self.input_str)
        print('pattern -->', self.pattern)
        print('priority --> ', self.priority_lst)
        print('reduced pattern', self.reduced_pattern_lst)
        print('reduced pattern', [self.reduced_pattern_lst[i] for i in self.priority_lst])
        print(is_match)
        print(self.match_matrix)

    def isMatch(self, input_str, pattern):
        self.pattern = pattern
        self.input_str = input_str

        self.reduced_pattern_lst = self._reduce_pattern()
        self.match_matrix = np.zeros((len(self.reduced_pattern_lst), len(self.input_str)))
        self.fillup_matrix()
        self.priority_lst = self.get_priority(self.reduced_pattern_lst)


        has_tmth_found = self.decision()
        if not has_tmth_found and (len(self.input_str) < 10):
            return False

        is_match = self.match_matrix.sum(0).sum() == len(self.input_str)
        is_rows_ones = self.match_matrix.sum(0).max() == 1
        # is_col_ones = self.match_matrix.sum(1).min() > 0
        is_match &= is_rows_ones

        self.aux_print(is_match)

        if is_match:
            return True

        self.aux_print(is_match)
        # print(self.match_matrix)

        try_count = 2

        if len(input_str) > 5:
            while not is_match and try_count >= 0:
                for ix, pattern_to_move in enumerate(self.priority_lst):

                    if not self.is_real_symbol(self.reduced_pattern_lst[pattern_to_move]):
                        break

                    is_match = self._here_we_go_again(
                        input_str,
                        pattern,
                        pattern_to_turn=pattern_to_move)
                    if is_match:
                        return True
                    try_count -= 1


        if len(input_str) > 5:
            try_count =  (len(self.input_str) - 1)
            while not is_match and try_count >= 0:
                for starting_point in range(1, len(self.input_str)):
                    for pattern_to_move in self.priority_lst:
                        for patter_to_turn in self.priority_lst:
                            if not self.is_real_symbol(self.reduced_pattern_lst[pattern_to_move]):
                                break

                            is_match = self._here_we_go_again(
                                input_str,
                                pattern,
                                pattern_to_turn=patter_to_turn,
                                pattern_to_move=pattern_to_move,
                                starting_point=starting_point)

                            try_count -= 1

                            if is_match:
                                self.aux_print(is_match)

                                return True

        self.aux_print(is_match)
        return is_match

u = Solution()
# u.isMatch('ab', '.*c')
# u.isMatch('aaaaaaaaaaaaaaaaaa', 'a*aaaa*aa.aaa.aaaa.a')
# print(u.reduced_pattern_lst, u.priority_lst)


