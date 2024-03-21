class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) <= 2:
            return s

        if numRows == 1:
            return s

        res_lst = [[] for _ in range(numRows)]
        zero_ix_num_rows = numRows - 1

        for i_symb, symb in enumerate(s):

            is_direct = (i_symb // zero_ix_num_rows) % 2 == False

            if is_direct:
                i_row = i_symb % zero_ix_num_rows
            else:
                i_row = (-1) * ((i_symb  % zero_ix_num_rows) + 1)

            res_lst[i_row].append(symb)

        res_lst = [''.join(lst) for lst in res_lst]

        res_str = ''.join(res_lst)

        return res_str


inp_str = 'PAYPALISHIRING'
n_rows = 3

print(Solution().convert(inp_str, n_rows))


