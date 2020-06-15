class MinStack(object):
    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, x):
        self.s.append(x)
        if self.min_s:
            if self.min_s[-1] > x:
                self.min_s.append(x)
            else:
                self.min_s.append(self.min_s[-1])
        else:
            self.min_s.append(x)

    def pop(self):
        if self.s:
            self.s.pop()
            self.min_s.pop()

    def top(self):
        if self.s:
            return self.s[-1]

    def getMin(self):
        if self.min_s:
            return self.min_s[-1]


if __name__ == '__main__':
    minStack = MinStack()

    minStack.push(2)
    minStack.push(1)
    minStack.push(4)
    print(minStack.top())
    minStack.pop()
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
    minStack.pop()
    minStack.push(7)
    print(minStack.top())
    print(minStack.getMin())
    minStack.push(4)
    print(minStack.top())
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
