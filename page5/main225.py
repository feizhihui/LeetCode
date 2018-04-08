# encoding=utf-8
from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.data.appendleft(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        return self.data.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return None
        return self.data[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.data) <= 0


if __name__ == '__main__':
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
