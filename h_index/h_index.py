from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations = sorted(citations)

        if len(citations) == 1:
            return int(citations[0] > 0)

        curr_ix = len(citations) - 1
        n_works = len(citations)

        while curr_ix >= 0:
            n_curr_works = n_works - curr_ix

            if citations[curr_ix] < n_curr_works:
                break

            curr_ix -= 1

        if (curr_ix == 0) and (citations[0] >= len(citations)):
            return len(citations)

        return n_curr_works - 1