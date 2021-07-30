
class Solution:
    def __init__(self):
        self.reverse_counter = -1
        self.curr_i = 0
        self.length = 0

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        self.curr_i += 1
        if head.next != None:
            self.removeNthFromEnd(head.next, n)
        else:
            #only one el
            if self.curr_i == 1:
                return None
            self.length = self.curr_i

        self.reverse_counter += 1

        if self.reverse_counter == n:
            head.next = head.next.next
            self.reverse_counter = n + 1

        #first el
        if self.length == n:
            return head.next

        return head

