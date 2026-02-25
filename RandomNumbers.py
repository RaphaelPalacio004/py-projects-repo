import random


def RandomNumbers():
    try:
        noRandoms = 20
        generateRandom = random.sample(range(0, 100), noRandoms)
        print(f"Unsorted list: {generateRandom}")
        result = []
        even_count = 0
        odd_count = 0

        for i, list_of_numbers in enumerate(generateRandom):
            generateRandom.sort()
            result = generateRandom
            print(f"Sorted list: {result}", "\n", end="")
            break
        for j in result:
            i += 1
            if j % 2 == 0:
                even_count += 1
                print(f"{j} is an even number")
            else:
                odd_count += 1
                print(f"{j} is an odd number")

        print(f"Even counter:{[even_count]}, Odd counter:{[odd_count]}")
        return i, j

    except Exception as exc:
        print(exc)


RandomNumbers()
