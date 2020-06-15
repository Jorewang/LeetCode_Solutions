from collections import Counter


class Solution(object):
    def groupAnagrams(self, strs):
        cout_li = [Counter(x) for x in strs]
        res = []
        visit = [0]*len(strs)

        for i, str in enumerate(strs):
            if visit[i] == 0:
                li = [str]
                visit[i] = 1
            else:
                continue
            k = i + 1
            while k<len(strs):
                if visit[k] == 0 and cout_li[i] == cout_li[k]:
                    visit[k] = 1
                    li.append(strs[k])
                k += 1
            res.append(li)
        return res

    def anagrams(self, strs):

        if len(strs) < 2 :
            return strs
        result=[]
        visited=[False]*len(strs)
        for index1,s1 in enumerate(strs):
            hasAnagrams = False
            for index2,s2 in enumerate(strs):
                if index2 > index1 and not visited[index2] and self.isAnagrams(s1,s2):
                    result.append(s2)
                    visited[index2]=True
                    hasAnagrams = True
            if not visited[index1] and hasAnagrams:
                result.append(s1)
        return result

    def isAnagrams(self, str1, str2):
        if sorted (str1) == sorted(str2):
                return True
        return False

    def groupAnagrams_2(self, strs):
        map = {}
        for str in strs:
            s = ''.join(sorted(str))
            if s in map:
                map[s].append(str)
            else:
                map[s] = [str]
        return list(map.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams_2(["eat", "tea", "tan", "ate", "nat", "bat"]))
