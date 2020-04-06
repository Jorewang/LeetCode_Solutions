class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, l, carry):
        if l1 == None and l2 == None :
            if carry != 0:
                newNode = ListNode(carry)
                l.next = newNode
            return 0
        elif l1 == None:
            newNode = ListNode((carry + l2.val)%10)
            carry = (carry + l2)//10
            l.next = newNode
            l = l.next
            l2 = l2.next
            self.addTwoNumbers(l1, l2, l, carry)
        elif l2 == None:
            newNode = ListNode((carry + l1.val)%10)
            carry = (carry + l1.val)//10
            l.next = newNode
            l = l.next
            l1 = l1.next
            self.addTwoNumbers(l1, l2, l, carry)
        else:
            newNode = ListNode((l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val + carry)//10
            l.next = newNode
            l = l.next
            l1 = l1.next
            l2 = l2.next
            self.addTwoNumbers(l1, l2, l, carry)

a = eval(input())
b = eval(input())

t1 = la = ListNode(None)
t2 = lb = ListNode(None)

for i in a:
    newNode = ListNode(i)
    t1.next = newNode
    t1 = t1.next
for i in b:
    newNode = ListNode(i)
    t2.next = newNode
    t2 = t2.next


l = ListNode(None)
s = Solution()
s.addTwoNumbers(la.next, lb.next, l, 0)

result = []
while l.next != None:
    result.append(l.next.val)
    l = l.next
print(result)