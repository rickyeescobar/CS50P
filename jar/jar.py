class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return self.size * "🍪"


    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceeded Capacity")
        if self.size + n > self.capacity:
            raise ValueError("Exceeded Capacity")
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Insufficient Cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(1)
    jar.withdraw(0)
    print(jar)


if __name__ == "__main__":
    main()