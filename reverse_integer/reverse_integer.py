class Solution(object):
    def reverse(self, x):
        if x == 0: return 0

        x_str = str(x)
        is_negative = False

        if x_str.startswith('-'):
            is_negative = True
            x_str = x_str[1:]

        x_str_reversed = x_str[::-1]

        while x_str[0] == '0':
            if len(x_str) > 1:
                x_str = x_str[1:]
            else:
                return 0

        int_reversed = int(x_str_reversed)
        if is_negative:
            int_reversed *= -1

        low_bound, high_bound = -2 ** 31, 2 ** 31 - 1
        if (int_reversed < low_bound) or (int_reversed > high_bound): return 0

        return int_reversed





print(Solution().reverse(-120))