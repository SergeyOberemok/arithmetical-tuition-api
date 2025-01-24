import random
from collections.abc import Generator, Iterable


def generateRandomNumbers(maxNumber: int, count: int) -> Generator[int, None, None]:
    numbers = [*range(1, maxNumber)]

    for _ in range(count):
        yield random.choice(numbers)


def generateRandomNumbersPairs(maxNumber: int, count: int) -> Iterable[Iterable[int]]:
    numbersPairs = zip(
        generateRandomNumbers(maxNumber, count),
        generateRandomNumbers(maxNumber, count),
    )

    return [*numbersPairs]
