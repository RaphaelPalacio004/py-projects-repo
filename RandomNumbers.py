import random
from loguru import logger


class GenerateRandomNumbers:
    def __init__(self, no_randoms, generate_random, result, even_count, odd_count):
        self.no_randoms = no_randoms
        self.generate_random = generate_random
        self.result = result
        self.even_count = even_count
        self.odd_count = odd_count

    def RandomNumbers(self):
        try:
            self.no_randoms = 20
            self.generate_random = random.sample(range(0, 100), self.no_randoms)
            print(f"Unsorted list: {self.generate_random}")
            self.result = []
            self.even_count = 0
            self.odd_count = 0
        except Exception:
            return logger.exception("The application encountered an error.")

    def __str__(self):
        for i, list_of_numbers in enumerate(self.generate_random):
            self.generate_random.sort()
            self.result = self.generate_random
            print(f"Sorted list: {self.result}", "\n", end="")
            break
        for j in self.result:
            i += 1
            if j % 2 == 0:
                self.even_count += 1
                print(f"{j} is an even number")
            else:
                self.odd_count += 1
                print(f"{j} is an odd number")

        return f"Even counter:{[self.even_count]}, Odd counter:{[self.odd_count]}"


Result = GenerateRandomNumbers(
    no_randoms="", generate_random=int, result=int, even_count=int, odd_count=int
)
Result.RandomNumbers()
print(Result)
