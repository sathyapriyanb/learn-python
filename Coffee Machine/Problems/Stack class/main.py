class Stack():

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)
        return self.peek()

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[- 1]

    def is_empty(self):
        return self.stack == []
