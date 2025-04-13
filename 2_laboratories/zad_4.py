from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

for _ in range(10):
    print(next(fib))

