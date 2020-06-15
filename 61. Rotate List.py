class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head
        li = []
        while head:
            li.append(head.val)
            head = head.next
        re = li[-(k % len(li)):] + li[:-(k % len(li))]

        head = ListNode(re.pop(0))
        tmp = head
        for i in re:
            node = ListNode(i)
            tmp.next = node
            tmp = node
        return head

    def rotateRight_2(self, head, k):
        if not head or k == 0:
            return head
        li = []

        while head:
            li.append(head)
            head = head.next

        k = k % len(li)

        li[-1].next = li[0]
        li[-k-1].next = None
        head = li[-k]
        return head
