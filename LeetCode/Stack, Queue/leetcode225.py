from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.cur_queue = 1
        self.length = 0
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.cur_queue == 1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

        self.length = self.length + 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        if self.cur_queue == 1:
            main_queue = self.queue1
            sub_queue = self.queue2
            self.cur_queue = 2
        else:
            main_queue = self.queue2
            sub_queue = self.queue1
            self.cur_queue = 1

        for i in range(self.length - 1):
            sub_queue.append(main_queue.popleft())

        self.length = self.length - 1

        return main_queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.cur_queue == 1:
            main_queue = self.queue1
            sub_queue = self.queue2
            self.cur_queue = 2
        else:
            main_queue = self.queue2
            sub_queue = self.queue1
            self.cur_queue = 1

        for i in range(self.length - 1):
            sub_queue.append(main_queue.popleft())

        cur_top = main_queue.popleft()
        sub_queue.append(cur_top)

        return cur_top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.length == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
