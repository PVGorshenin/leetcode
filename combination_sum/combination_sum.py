from typing import List



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if target < min(candidates):
            return []

        res_lst = self.dfs(candidates, target)
        return res_lst


    def dfs(self, candidates, target):

        res_lst = []

        for i_num, num in enumerate(candidates):
            if num > target:
                candidates.pop(i_num)

        for i_num, num in enumerate(candidates):
            if target == num:
                res_lst.append([num])

            curr_res_lst = self.dfs(candidates[i_num:], target-num)
            res_lst.extend([[num] + found_lst for found_lst in curr_res_lst])

        return res_lst
