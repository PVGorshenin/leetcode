from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        interval_dict = {}
        seen_set = set()

        if len(nums) == 0:
            return 0

        max_len = 1

        for num in nums:

            if num in seen_set:
                continue

            if num not in interval_dict.keys():

                left_neighbour = num - 1
                right_neighbour = num + 1

                if left_neighbour in interval_dict.keys():
                    interval_dict[left_neighbour][1] = num
                else:
                    interval_dict[left_neighbour] = [left_neighbour, num]

                if right_neighbour in interval_dict.keys():
                    interval_dict[right_neighbour][0] = num
                else:
                    interval_dict[right_neighbour] = [num, right_neighbour]

            else:

                left_neighbour = interval_dict[num][0] - 1
                right_neighbour = interval_dict[num][1] + 1

                curr_len = interval_dict[num][1] - interval_dict[num][0] + 1
                max_len = max(max_len, curr_len)

                if left_neighbour in interval_dict.keys():
                    interval_dict[left_neighbour][1] = interval_dict[num][1]
                else:
                    interval_dict[left_neighbour] = [left_neighbour, interval_dict[num][1]]

                if right_neighbour in interval_dict.keys():
                    interval_dict[right_neighbour][0] = interval_dict[num][0]
                else:
                    interval_dict[right_neighbour] = [interval_dict[num][0], right_neighbour]

                interval_dict.pop(num)

            seen_set.add(num)

        return max_len
