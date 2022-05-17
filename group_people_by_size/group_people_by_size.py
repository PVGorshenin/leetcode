from collections import Counter
from time import time
from typing import List

class Solution:

    def _get_sorted(self, groupSizes):
        list_of_tuples = [(i, v) for (i, v) in enumerate(groupSizes)]
        sorted_input = sorted(list_of_tuples, key=lambda tuple_: tuple_[1])
        return sorted_input

    def _check_input(self, groupSizes):
        len_of_input = len(groupSizes)
        assert (len_of_input > 0) & (len_of_input <= 500)
        assert max(groupSizes) <= 500
        assert sum([tuple_[1] % tuple_[0] for tuple_ in Counter(groupSizes).most_common()]) == 0

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # self._check_input(groupSizes)
        sorted_input = self._get_sorted(groupSizes)
        current_group_ind, output = [], []
        for tuple_ in sorted_input:
            ind, size_of_group = tuple_
            current_group_ind.append(ind)
            if len(current_group_ind) == size_of_group:
                output.append(current_group_ind)
                current_group_ind = []
        if len(current_group_ind): output.append(current_group_ind)
        return output

start_time = time()
Solution().groupThePeople(groupSizes=[2,2,1,3,3,3])
finish_time = time()
print(finish_time - start_time)




