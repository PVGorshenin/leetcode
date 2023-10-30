from typing import List


class Solution:

    def find_belonging_groups(self, connected_groups, i_row, i_col):
        found_groups = []
        for i_group, group in enumerate(connected_groups):
            for point in reversed(group['connected_seq']):
                is_neighbour = ((abs(i_row - point[0]) == 1) &  (i_col == point[1]) |
                                 (abs(i_col - point[1]) == 1) & (i_row == point[0]))
                if is_neighbour:
                    found_groups.append(i_group)
                    break

        return found_groups

    def merge_or_extend_groups(self, found_groups, connected_groups, point, is_on_border):
        if len(found_groups) > 1:
            for i_group in found_groups[1:]:
                connected_groups[found_groups[0]]['connected_seq'].extend(
                    connected_groups[i_group]['connected_seq'])

                connected_groups[found_groups[0]]['is_on_border'] |= connected_groups[i_group]['is_on_border']
                connected_groups.pop(i_group)

        connected_groups[found_groups[0]]['connected_seq'].extend([point])
        connected_groups[found_groups[0]]['is_on_border'] |= is_on_border

        return connected_groups

    def color_surrounded_by_x(self, board):

        min_side_len = min(len(board), len(board[0]))

        for step_from_border in range(min_side_len // 2):

            high_row = board[step_from_border][step_from_border:-step_from_border-1]
            low_row = board[-step_from_border - 1][step_from_border:-step_from_border - 1]
            left_col = [item[step_from_border] for item in board[step_from_border:-step_from_border-1]]
            right_col = [item[-step_from_border-1] for item in board[step_from_border:-step_from_border-1]]

            rechtangle_set = set(high_row) | set(low_row) | set(left_col) | set(right_col)

            if rechtangle_set == set("X"):

                for i_step in range(step_from_border, len(board[0])-step_from_border):
                    fill_up_val = ["X"] * (len(board[i_step][step_from_border:-step_from_border-1]))
                    board[i_step][step_from_border:-step_from_border-1] = fill_up_val

                return board, step_from_border

        return board, None

    def recolor_inner_groups(self, connected_groups, board):
        for i_group, group in enumerate(connected_groups):

            if not group['is_on_border']:
                for point in group['connected_seq']:
                    board[point[0]][point[1]] = "X"

        return board

    def solve(self, board: List[List[str]]) -> None:

        connected_groups = []
        n_rows = len(board)
        n_cols = len(board[0])

        if n_rows == 1:
            return board

        if board == []:
            return board

        board, next_already_colored = self.color_surrounded_by_x(board)

        for i_row in range(n_rows):
            for i_col in range(n_cols):

                if next_already_colored is not None:
                    if ((i_row // 2) > next_already_colored) and ((i_col // 2) > next_already_colored):
                        continue

                if board[i_row][i_col] == 'O':
                    is_on_border = ((i_row == 0) | (i_col == 0) |
                                    (i_row == n_rows - 1) | (i_col == n_cols - 1))

                    found_groups = self.find_belonging_groups(connected_groups, i_row, i_col)

                    point = (i_row, i_col)

                    if len(found_groups):
                        connected_groups = self.merge_or_extend_groups(
                            found_groups,
                            connected_groups,
                            point,
                            is_on_border)

                    else:
                        connected_groups.append({
                            'is_on_border': is_on_border,
                            'connected_seq': [point]
                        })

        return self.recolor_inner_groups(connected_groups, board)






