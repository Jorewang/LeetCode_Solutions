import sys
import copy
class Solution(object):
    def numBusesToDestination(self, routes, S, T):

        ans = sys.maxsize

        def recur(begin, routes, cur, T):
            nonlocal ans
            li = copy.deepcopy(routes)
            for route in li:
                if set(route) & begin:
                    if route.count(T) != 0:
                        if cur+1 < ans:
                            ans = cur + 1
                        continue
                    routes.remove(route)
                    recur(set(route), routes, cur + 1, T)
                    routes.append(route)

        li = set()
        li.add(S)
        recur(li, routes, 0, T)
        return ans if ans != sys.maxsize else -1

    def numBusesToDestination_2(self, routes, S, T):
        if S is None or T is None:
            return -1
        if S == T:
            return 0
        li_s = []
        li_t = []
        count_s = count_t = 0
        visit_s = [0]*len(routes)
        visit_t = [0]*len(routes)
        for id, route in enumerate(routes):
            if route.count(S) != 0:
                count_s += 1
                visit_s[id] = 1
                li_s.append(route)
            if route.count(T) != 0:
                count_t += 1
                visit_t[id] = 1
                li_t.append(route)
        if not li_s or not li_t:
            return -1
        cur_s = 1
        cur_t = 1
        for route in li_s:
            if route in li_t:
                return cur_s + cur_t - 1
        while li_s or li_t:
            if li_s:
                c = 0
                while count_s > 0:
                    rt = li_s.pop(0)
                    for id, route in enumerate(routes):
                        if visit_s[id] == 0 and set(route) & set(rt):
                            c += 1
                            visit_s[id] = 1
                            li_s.append(route)
                    count_s -= 1
                count_s = c
                cur_s += 1
            for route in li_s:
                if route in li_t:
                    return cur_s + cur_t - 1
            if li_t:
                c = 0
                while count_t > 0:
                    rt = li_t.pop(0)
                    for id, route in enumerate(routes):
                        if visit_t[id] == 0 and set(route) & set(rt):
                            c += 1
                            visit_t[id] = 1
                            li_t.append(route)
                    count_t -= 1
                count_t = c
                cur_t += 1
            for route in li_s:
                if route in li_t:
                    return cur_s + cur_t - 1
        return -1






if __name__ == '__main__':
    routes =  [[0,4,15],[17,20],[4,11,14,16,23],[1,12,15,16],[0,6,8,10]]
    print(Solution().numBusesToDestination_2(routes, 0, 10))