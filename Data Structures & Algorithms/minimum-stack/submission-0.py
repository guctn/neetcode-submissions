class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val:
            self.min_val.append(val)
        else:
            if self.min_val[-1] >= val:
                self.min_val.append(val)

    def pop(self) -> None:
        removed_val = self.stack.pop()
        
        if removed_val == self.min_val[-1]:
            self.min_val.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]

        
