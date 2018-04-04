# encoding=utf-8

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.length = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.length += 1

    def pop(self):
        """
        :rtype: void
        """
        val = self.stack[self.length - 1]
        del self.stack[self.length - 1]
        self.length -= 1
        return val

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.length - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_2, param_3, param_4)
