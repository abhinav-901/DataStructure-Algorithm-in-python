
class Stack:
    """Implementation of stack using python list
    list - Thread safe (No)

    dequeue - Thread safe (Yes but not fully)

    lifoqueue - Thread safe (Yes full thread safety)

    So use lifoqueue if need full thread safety and performance is not the bottleneck"""

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def get_stack(self):
        return self.stack

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
