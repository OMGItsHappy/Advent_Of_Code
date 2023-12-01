class test:
    def __init__(self) -> None:
        self.a = 1

b = test()

c = test(b)

c.a += 1

print(b.a)