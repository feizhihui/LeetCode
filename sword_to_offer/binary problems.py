# encoding=utf-8

"""
把一个整数减去1之后再和原来的整数做位与运算
得到的结果相当于是把整数的二进制表示中的最右边一个1变成0
"""


def one_in_binary(num):
    """
    二进制中1的个数
    python的int 也是个object类型
    """
    count = 0
    while num:
        num = num & (num - 1)
        count += 1
    return count


ans = one_in_binary(10)
print(ans)


def is_power_of_two(num):
    """
    二进制中1的个数
    python的int 也是个object类型
    """
    num = num & (num - 1)
    return num == 0


b = is_power_of_two(32)
print(b)
