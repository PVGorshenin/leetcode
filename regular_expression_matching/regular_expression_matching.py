class Solution(object):
    def __init__(self):
        self.i_pattern = 0
        self.i_str = 0
        self.multiple_patterns = set()

    def _get_quantifier(self):
        if self.i_pattern < len(self.pattern)-1:
            if self.pattern[self.i_pattern+1] == '*':
                self.i_pattern += 1
                return '*'
        return None

    def _get_next_pattern(self):
        if self.i_pattern < len(self.pattern)-1:
            return self.pattern[self.i_pattern+1]
        return None

    def _get_next_next_pattern(self):
        if self.i_pattern < len(self.pattern)-1:
            return self.pattern[self.i_pattern+1]
        return None

    def is_pattern_fully_satisfied(self, pattern, next_pattern):
        if self.i_str < len(self.input_str)-1:
            next_symbol = self.input_str[self.i_str+1]
            if (next_symbol == pattern) & (pattern != next_pattern):
                return False
        return True

    def _check_pattern_collapsed(self):
        least_len = len(self.pattern) - self.i_pattern
        for i_letter in range(least_len-1):
            if (self.pattern[self.i_pattern] != '*') & (self.pattern[self.i_pattern+1] != '*'):
                if self.pattern[self.i_pattern] in self.multiple_patterns:
                    self.multiple_patterns = set()
                else:
                    return False
            self.i_pattern += 1
        if (self.pattern[-1] != '*') & (not self.pattern[-1] in self.multiple_patterns):
            return False
        return True

    def shift_next_pattern(self):
        self.i_pattern += 1
        next_pattern = self._get_next_next_pattern()
        return next_pattern

    def _check_str_or_pattern_finished(self):
        is_patern_finished = self.i_pattern == len(self.pattern)
        is_str_finished = self.i_str == len(self.input_str)
        return is_patern_finished | is_str_finished

    def _check_str_n_pattern_finished(self):
        is_patern_finished = self.i_pattern == len(self.pattern)
        if not is_patern_finished:
            is_patern_finished |= self._check_pattern_collapsed()
        is_str_finished = self.i_str == len(self.input_str)
        return is_patern_finished & is_str_finished

    def _check_letter_symbol(self, curr_pattern):
        if self.input_str[self.i_str] == curr_pattern:
            self.i_str += 1
            return True
        return False

    def _check_letter_pattern(self, curr_pattern):
        is_match_found = self._check_letter_symbol(curr_pattern)
        if (not is_match_found) & (curr_pattern in self.multiple_patterns):
            is_match_found = True
        if is_match_found: self.i_pattern += 1
        return is_match_found

    def _check_letter_pattern_quantifier(self, curr_pattern, next_pattern):
        self.multiple_patterns.add(curr_pattern)
        is_match_found = False
        while not self._check_str_or_pattern_finished():
            is_curr_match = self._check_letter_symbol(curr_pattern)
            is_match_found |= is_curr_match
            if is_curr_match:
                if curr_pattern == next_pattern:
                    next_pattern = self.shift_next_pattern()
            if not is_curr_match:
                break
        self.i_pattern += 1
        return is_match_found

    def _check_any_pattern(self, next_pattern, quantifier):
        if quantifier is None:
            self.i_str += 1
            self.i_pattern += 1
        if quantifier is '*':
            while not self._check_str_or_pattern_finished():
                if self.input_str[self.i_str] == next_pattern:
                    # .*a == a*
                    next_next_pattern = self._get_next_next_pattern()
                    self.i_str += 1
                    self.i_pattern += 1
                    self._check_letter_pattern_quantifier(next_pattern, next_next_pattern)
                    return
                if next_pattern == '.':
                    next_pattern = self.shift_next_pattern()
                self.i_str += 1
            self.i_pattern += 1

    def isMatch(self, input_str, pattern):
        self.pattern = pattern
        self.input_str = input_str
        while not(self._check_str_or_pattern_finished()):
            curr_pattern = pattern[self.i_pattern]
            quantifier = self._get_quantifier()
            next_pattern = self._get_next_pattern()
            if curr_pattern != '.':
                if quantifier is None:
                    is_curr_match = self._check_letter_pattern(curr_pattern)
                    if is_curr_match:
                        self.multiple_patterns = set()
                    else:
                        return False
                elif quantifier is '*':
                    is_curr_match_quant = self._check_letter_pattern_quantifier(curr_pattern, next_pattern)
                    if is_curr_match_quant:
                        self.multiple_patterns = set(curr_pattern)
            elif curr_pattern == '.':
                self._check_any_pattern(next_pattern, quantifier)
        if self._check_str_n_pattern_finished():
            return True
        return False




