class Solution(object):
    def __init__(self):
        self.i_pattern = 0
        self.i_str = 0

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

    def _check_pattern_collapsed(self):
        least_str = self.pattern[self.i_pattern:]
        for i_letter in range(len(least_str)-1):
            if (least_str[i_letter] != '*') & (least_str[i_letter+1] != '*'):
                return False
        if least_str[-1] != '*':
            return False
        return True

    def _check_any_finished(self):
        is_patern_finished = self.i_pattern == len(self.pattern)
        is_str_finished = self.i_str == len(self.input_str)
        return is_patern_finished | is_str_finished

    def _check_all_finished(self):
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

    def _check_letter_pattern(self, curr_pattern, quantifier):
        is_match_found = False
        if quantifier is None:
            is_match_found = self._check_letter_symbol(curr_pattern)
            self.i_pattern += 1
        if quantifier is '*':
            while not self._check_any_finished():
                is_match_found = True
                is_curr_match = self._check_letter_symbol(curr_pattern)
                if not is_curr_match: break
            self.i_pattern += 1
        return is_match_found

    def _check_any_pattern(self, next_pattern, quantifier):
        if quantifier is None:
            self.i_str += 1
            self.i_pattern += 1
        if quantifier is '*':
            while not self._check_any_finished():
                is_curr_match = self._check_letter_symbol(next_pattern)
                if is_curr_match: break
            self.i_pattern += 1

    def isMatch(self, input_str, pattern):
        self.pattern = pattern
        self.input_str = input_str
        while not(self._check_any_finished()):
            curr_pattern = pattern[self.i_pattern]
            quantifier = self._get_quantifier()
            nex_pattern = self._get_next_pattern()
            if curr_pattern != '.':
                is_curr_match = self._check_letter_pattern(curr_pattern, quantifier)
            if curr_pattern == '.':
                self._check_any_pattern(nex_pattern, quantifier)
            if not is_curr_match:
                return False
        if self._check_all_finished():
            return True
        return False




