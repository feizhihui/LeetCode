# encoding=utf-8

def dfs(clist):
    if len(clist) == 0:
        return []
    root = clist[0]
    res = []
    for i in range(1, len(clist)):
        left = dfs(clist[1:i])
        right = dfs(clist[i:])
        ans = inner_join(left, root, right)
        res.extend(ans)
    if len(res) == 0:
        return [[root]]
    return res


def inner_join(left, root, right):
    ans = []
    if len(left) != 0 and len(right) != 0:
        for l1 in left:
            for l2 in right:
                ans.append(l1 + l2 + [root])
    elif len(left) == 0:
        for l2 in right:
            ans.append(l2 + [root])
    elif len(right) == 0:
        for l1 in left:
            ans.append(l1 + [root])
    return ans


n = int(input())
clist = [chr(i + 97) for i in range(n)]
# clist = list(input())

ans = dfs(clist)
for line in ans:
    res = ''.join(line)
    print(res)
print(len(ans))
