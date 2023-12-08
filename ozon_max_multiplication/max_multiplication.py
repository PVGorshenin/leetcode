def find_max_multiplication(nums):
    neg_lst, pos_lst = [], []

    if len(nums) == 2:
        return nums[0] * nums[1]

    max_multiplication = 0

    for num in nums:

        if num == 0: continue

        is_positive = False
        if num > 0: is_positive = True

        if is_positive:

            if len(pos_lst) == 0:
                pos_lst.append(num)

            if len(pos_lst) == 1:
                pos_lst.append(num)
                pos_lst = sorted(pos_lst)

            if len(pos_lst) == 2:
                if num > pos_lst[0]:
                    pos_lst[0] = num
                    pos_lst = sorted(pos_lst)

        else:

            if len(neg_lst) == 0:
                neg_lst.append(num)

            if len(pos_lst) == 1:
                neg_lst.append(num)
                neg_lst = sorted(neg_lst)

            if len(neg_lst) == 2:
                if num < neg_lst[1]:
                    neg_lst[1] = num
                    neg_lst = sorted(neg_lst)

    if len(pos_lst) == 2:
        max_multiplication = pos_lst[0] * pos_lst[1]

    if len(neg_lst) == 2:
        max_multiplication = max(
            max_multiplication,
            neg_lst[0] * neg_lst[1]
        )

    return max_multiplication
