class Solution:
    def isValid(self, s: str) -> bool:
        stack_lst = []

        open_parentheses = ['{', '[', '(']
        close_parentheses = ['}', ']', ')']

        for char in s:
            if len(stack_lst):

                if char in open_parentheses:
                    if char == stack_lst[-1][0]:
                        stack_lst[-1][1] += 1
                    else:
                        stack_lst.append([char, 1])
                else:
                    open_match = open_parentheses[close_parentheses.index(char)]

                    if open_match == stack_lst[-1][0]:
                        stack_lst[-1][1] -= 1

                        if stack_lst[-1][1] == 0:
                           stack_lst = stack_lst[:-1]
                    else:
                        return False

            else:
                stack_lst.append([char, 1])

        if len(stack_lst) > 0:
            return False

        return True

