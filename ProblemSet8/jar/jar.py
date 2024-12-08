class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Invalid number.")
        self.cap = capacity
        self.num = 0

    def __str__(self):
        return self.num * "🍪"

    def deposit(self, n):
        self.num = self.num + n
        if self.num > self.cap:
            raise ValueError("Capacity limits are exceeded")
        if not isinstance(n, int) or n < 0:
            raise ValueError("Invalid number.")

    def withdraw(self, n):
        self.num = self.num - n
        if self.num < 0:
            raise ValueError("There are not so many cookies")
        if not isinstance(n, int) or n < 0:
            raise ValueError("Invalid number.")
        return self.num

    @property
    def capacity(self):
        return self.cap

    @property
    def size(self):
        return self.num

# jar = Jar(3)
# jar.deposit(3)
# print(jar)
# jar.withdraw(1)
# print(jar)
