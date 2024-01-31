from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i_left, i_right = 0, 0

        chars_freq = defaultdict(int)
        chars_freq[s[0]] = 1
        most_freq_char = s[0]
        i_right = 1
        max_window = 1

        while i_right < len(s):
            window_size = i_right - i_left + 1
            curr_char = s[i_right]
            chars_freq[curr_char] += 1

            if chars_freq[curr_char] > chars_freq[most_freq_char]:
                most_freq_char = curr_char

            if window_size - chars_freq[most_freq_char] > k:
                chars_freq[s[i_left]] -= 1
                i_left += 1
            else:
                max_window = max(max_window, window_size)

            i_right += 1

        return max_window


print(Solution().characterReplacement('aaaabb', 2))





