from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if target < min(candidates):
            return []

        is_sum_found, res_lst = self.dfs(candidates, target)
        return res_lst


    def dfs(self, candidates, target):

        res_lst = []
        is_sum_found = False

        for i_num, num in enumerate(candidates):
            if num > target:
                candidates.pop(i_num)

        for i_num, num in enumerate(candidates):
            if target == num:
                is_sum_found = True
                res_lst.append([num])

            is_curr_sum_found, curr_res_lst = self.dfs(candidates[i_num:].copy(), target-num)
            res_lst.extend([[num] + found_lst for found_lst in curr_res_lst])
            is_sum_found |= is_curr_sum_found

        return is_sum_found, res_lst




