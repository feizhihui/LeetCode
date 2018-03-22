# encoding=utf-8

from collections import deque

"""

广度优先搜索求解两个状态的最短路径

"""


def bfs(list1, list2):
    ans = deque()
    state_map = set(tuple(list1))
    ans.append(tuple(list1))
    step = 0
    while len(ans) > 0:
        backup = deque()
        for nums in ans:
            if tuple(nums) == tuple(list2):
                return step
            a_state = list(nums)
            for i, num in enumerate(nums):
                # try plus one
                a_state[i] = num + 1
                if tuple(a_state) not in state_map:
                    state_map.add(tuple(a_state))
                    backup.append(tuple(a_state))
                a_state[i] = num - 1
                # try minus one
                if tuple(a_state) not in state_map:
                    state_map.add(tuple(a_state))
                    backup.append(tuple(a_state))
                # try change two elements
                a_state = list(nums)
                for j in range(i + 1, len(nums)):
                    a_state[i], a_state[j] = a_state[j], a_state[i]
                    if tuple(a_state) not in state_map:
                        state_map.add(tuple(a_state))
                        backup.append(tuple(a_state))
                    a_state[i], a_state[j] = a_state[j], a_state[i]

        ans = backup
        step += 1


if __name__ == '__main__':
    step = bfs([3, 4, 5, 4, 4, 3, 3], [5, 4, 3, 2, 2, 3, 3])
    print(step)
