class MinStack:

    def __init__(self):
        self.mystackBitch: List = []

    def push(self, val: int) -> None:
        self.mystackBitch.append(val)

    def pop(self) -> None:
        self.mystackBitch.pop()

    def top(self) -> int:
        return self.mystackBitch[-1]

    def getMin(self) -> int:
        return min(self.mystackBitch)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()