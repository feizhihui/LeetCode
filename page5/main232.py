# encoding=utf-8

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.s1:
            self.s2.append(self.s1.pop(-1))
        val = self.s2.pop(-1)
        while self.s2:
            self.s1.append(self.s2.pop(-1))
        return val

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.s1:
            self.s2.append(self.s1.pop(-1))
        val = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2.pop(-1))
        return val

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1) <= 0


if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
