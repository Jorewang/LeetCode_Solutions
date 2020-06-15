class Solution(object):
    def validateStackSequences(self, pushed, popped):
        if not pushed and not popped:
            return True
        pushed_seq = [pushed.pop(0)]
        while pushed:
            if pushed_seq and pushed_seq[-1] == popped[0]:
                popped.pop(0)
                pushed_seq.pop(-1)
            else:
                while pushed and (not pushed_seq or pushed_seq[-1] != popped[0]):
                    pushed_seq.append(pushed.pop(0))
        return pushed_seq[::-1] == popped

    def validateStackSequences_2(self, pushed, popped):
        i, stack = 0, []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack


if __name__ == '__main__':
    print(Solution().validateStackSequences_2([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
