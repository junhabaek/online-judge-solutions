class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_stack = []
        self.temp_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.main_stack:
            self.temp_stack.append(self.main_stack.pop())
        self.temp_stack.append(x)

        while self.temp_stack:
            self.main_stack.append(self.temp_stack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.main_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # stack adt상 top이 있으므로, list[-1]을 그냥 사용
        return self.main_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.main_stack:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
