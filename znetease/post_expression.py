# encoding=utf-8
"""
10
( a + b ) * c
"""

from collections import deque

priority = {'+': 0, '-': 0, '*': 1, '/': 1, ')': -1, '(': -1}


# 遇到优先级低于栈顶的符号，则将栈顶元素打印


def expression(exp):
    """"""
    stack = deque()
    n = 0
    for e in exp:
        if e not in priority:
            print(e, end='')
        elif len(stack) == 0 or e == '(':
            stack.append(e)
            n += 1
        elif e == ')':
            top = stack[n - 1]
            while top != '(' and n >= 1:
                print(stack.pop(), end='')
                n -= 1
                top = stack[n - 1]

            stack.pop()
            n -= 1
        else:
            top = stack[n - 1]
            # 遇到优先级低于栈顶的符号，则将栈顶元素打印
            while n >= 1 and priority[e] < priority[top]:
                print(stack.pop(), end='')
                n -= 1
            stack.append(e)
            n += 1
    while len(stack) > 0:
        print(stack.pop(), end='')
    print()


if __name__ == '__main__':
    n = int(input())
    exp = input().split()
    expression(exp)
