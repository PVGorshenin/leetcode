from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        n_steps = 0
        min_steps = 100

        if endGene not in bank:
            return -1

        min_steps, is_match_found = self.dfs(startGene, endGene, bank.copy(), n_steps, min_steps)

        if is_match_found:
            return min_steps

        return -1

    def dfs(self, startGene, endGene, bank, n_steps, min_steps):

        adjacent_lst = []
        n_steps += 1
        is_match_found = False

        if endGene == startGene:
            return n_steps, True

        for curr_gene in bank:
            curr_dist = 0
            for i_symb in range(len(endGene)):

                if curr_gene[i_symb] != startGene[i_symb]:
                    curr_dist += 1

                if curr_dist > 1:
                    break

            if curr_dist == 1:
                if curr_gene == endGene:
                    return n_steps, True

                adjacent_lst.append(curr_gene)

        if n_steps > 1:
            bank.remove(startGene)

        for next_gene in adjacent_lst:
            curr_min_steps, is_curr_match_found = self.dfs(next_gene, endGene, bank.copy(), n_steps, min_steps)
            is_match_found |= is_curr_match_found

            if is_curr_match_found:
                min_steps = min(curr_min_steps, min_steps)

        return min_steps, is_match_found

startGene = "AAAACCCC"
endGene = "CCCCCCCC"
bank = ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]

print(Solution().minMutation(startGene, endGene, bank))


