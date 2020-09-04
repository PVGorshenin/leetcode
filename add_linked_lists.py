class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def _get_simple_list(self, list_node):
        lst = []
        while list_node.next:
            lst.append(list_node.val)
            list_node = list_node.next
        if list_node.val is not None:
            lst.append(list_node.val)
        return lst

    def _get_final_node(self, list_of_int):
        start = ListNode(int(list_of_int[0]))
        prev = start
        for digit in list_of_int[1:]:
            now = ListNode(digit)
            prev.next = now
            prev = now
        return start

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lst1 = self._get_simple_list(l1)
        lst2 = self._get_simple_list(l2)
        lst1.reverse()
        lst2.reverse()
        lst1 = [str(i) for i in lst1]
        lst2 = [str(i) for i in lst2]
        number = int(''.join(lst1)) + int(''.join(lst2))
        list_of_str = list(str(number))
        list_of_str.reverse()
        list_of_int = [int(i) for i in list_of_str]
        return self._get_final_node(list_of_int)


l1 = ListNode(0)
# l1.next = ListNode(4)
l2 = ListNode(0)


res = Solution().addTwoNumbers(l1, l2)

while res.next:
    print(res.val)
    res = res.next
print(res.val)
