from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        q = deque()
        res = []

        i = 0
        count = 0

        def find_next_maximum_number(j: int, q: deque[int], n: int) -> int:
            next_maximum_number = 0

            for i in range(1, n):
                if q[i] > j:
                    next_maximum_number = j

            return next_maximum_number
            

        while i < n:
            q.append(temperatures[i])

            if find_next_maximum_number(q[0], q, len(q)) > q[0]:
                q.popleft()
                res.append(count)
                count = 0

            i += 1
            count += 1

        r = 1
        r_count = 1

        while r < len(q):
            if q[r] > q[0]:
                q.popleft()
                res.append(r_count)

                r_count = 1
                r = 1

                continue # one change with AI

            r += 1
            r_count += 1

            if r >= len(q):
                res.append(0)
                q.popleft()
                r_count = 1
                r = 1
                continue

        if len(q) == 1:
            res.append(0)

        return res
