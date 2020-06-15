class Solution(object):
    def reorderLogFiles(self, logs):

        letter_log = {}
        letter_logs = []
        res = []

        for idx, log in enumerate(logs):
            if log.split(' ')[-1].isdigit():
                res.append(log)
            else:
                letters = tuple(log.split(' ')[1:])
                letter_log[letters] = idx
                letter_logs.append(letters)

        letter_logs.sort(reverse=True)

        for letters in letter_logs:
            res.insert(0, logs[letter_log[letters]])

        return res


if __name__ == '__main__':
    print(Solution().reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
