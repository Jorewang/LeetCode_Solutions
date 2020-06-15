class Solution(object):
    def myAtoi(self, str):

        str = str.lstrip()
        if not str or (str[0] != '-' and str[0] != '+' and not str[0].isdigit()):
            return 0

        is_T = False
        val = 0
        if str[0] == '-':
            is_T = True
        elif str[0] == '+':
            pass
        else:
            val = val * 10 + int(str[0])
        for nul in str[1:]:
            if not nul.isdigit():
                break
            else:
                val = val * 10 + int(nul)

        val = -val if is_T else val

        if -(1 << 31) <= val <= (1 << 31) - 1:
            return val
        else:
            if val < -(1 << 31):
                return -(1 << 31)
            else:
                return (1 << 31) - 1


if __name__ == '__main__':
    print(Solution().myAtoi("+1"))
