# encoding=utf-8

from collections import defaultdict

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(list)  # 定义value类型
for k, v in s:
    d[k].append(v)
print(d)

# ==============================================
from collections import OrderedDict

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
d = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
print(d)
e = d.popitem()
print(e, d)
d.move_to_end('orange', last=True)
print(d)
# ==============================================
from collections import deque

d = deque([1, 2, 3])
print(d.pop(), d)

# ==============================================
from collections import ChainMap

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
m = ChainMap(a, b)
print(m['c'])
print(m.maps)
m2 = m.new_child()
print(m2)
print(m2.parents)

# ==============================================
from collections import Counter

a = [1, 4, 2, 3, 2, 3, 4, 2]
c = Counter(a)
print(c)
print(c.most_common(1))

# ==============================================
from collections import namedtuple

Point = namedtuple('PointExtension', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x, p.y)

# ==============================================
if __name__ == '__main__':
    pass
