from typing import List


class Solution:

    def _find_global_max_n_submax(self, least_hights):

        global_max, prev_max = 0, 0
        i_max, prev_i_max = [0], [0]
        for i, val in enumerate(least_hights):
            if val > global_max:
                prev_max = global_max
                prev_i_max = i_max

                global_max = val
                i_max = [i]
            elif val == global_max:
                i_max.append(i)
            elif val > prev_max:
                prev_i_max = [i]
                prev_max = val
            elif val == prev_max:
                prev_i_max.append(i)

        return i_max, prev_i_max, prev_max, global_max


    def crop_borders_slope(self, height):

        i_min, i_max = len(height), 0
        for i in range(len(height)-1):
            if height[i+1] < height[i]:
                i_min = i
                break
        height = height[i_min:]

        for i in range(len(height)-1, 0, -1):
            if height[i] > height[i-1]:
                i_max = i
                break
        height = height[:i_max + 1]
        return height

    def trap(self, height: List[int]) -> int:

        least_hights = self.crop_borders_slope(height)
        trapped = 0
        if len(height) <= 2:
            return trapped

        i_max, prev_i_max, prev_max, global_max = self._find_global_max_n_submax(least_hights)
        submax = prev_max

        if len(i_max) > 1:
            submax = global_max
            min_start = i_max[0]
            min_finish = i_max[-1]
        elif len(prev_i_max) > 1:
            min_start = prev_i_max[0]
            min_finish = max(prev_i_max[-1], i_max[0])
        else:
            min_start = min(prev_i_max[0], i_max[0])
            min_finish = max(prev_i_max[0], i_max[0])

        for j in range(min_start, min_finish):
            trapped += max(submax - least_hights[j], 0)

        trapped += self.trap(least_hights[:min_start + 1])
        trapped += self.trap(least_hights[min_finish:])


        return trapped




print(len(Solution().crop_borders_slope(list(range(10000)))))