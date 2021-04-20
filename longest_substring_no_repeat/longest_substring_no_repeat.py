class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_window_size = len(set(s))
        for window_size in range(max_window_size, 0, -1):
            steps_possible = len(s) - window_size + 1
            for i_start in range(steps_possible):
                current_s = s[i_start:i_start+window_size]
                if len(current_s) == len(set(current_s)):
                    return len(current_s)
        return 0


