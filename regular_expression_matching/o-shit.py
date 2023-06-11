if start_w_median and (curr_row == change_pattern_turn):
    coll_median = self.match_matrix.shape[1] // 2
    for i_col in range(coll_median):
        if self.match_matrix[
           curr_row,
           coll_median + i_col: coll_median + i_col + len(curr_pattern)].sum() == len(curr_pattern):
            has_match_found = True
            self.add_zeros_to_matrix(
                curr_row,
                coll_median + i_col,
                len(curr_pattern))

        if self.match_matrix[
           curr_row,
           coll_median - i_col - len(curr_pattern): coll_median - i_col].sum() == len(curr_pattern):
            has_match_found = True
            self.add_zeros_to_matrix(
                curr_row,
                coll_median - i_col - len(curr_pattern),
                len(curr_pattern))