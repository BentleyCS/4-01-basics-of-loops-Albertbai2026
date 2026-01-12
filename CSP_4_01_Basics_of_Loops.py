import random

# All questions must use a loop for full points.

def oddNumbers(n: int) -> str:
    """
    Print out all odd numbers from 1 to n (inclusive) in a single string separated by spaces.
    """
    result = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            result.append(str(i))
    return " ".join(result)


def backwards(n: int) -> str:
    """
    Print all numbers from n down to 1.
    """
    if n <= 0:
        return ""
    result = []
    for i in range(n, 0, -1):
        result.append(str(i))
    return " ".join(result)


def randomRepeating():
    """
    Print random numbers from 1–10 until a 10 appears, then print tries.
    """
    tries = 0
    roll = 0
    while roll != 10:
        roll = random.randint(1, 10)
        print(roll)
        tries += 1
    print(f"it took {tries} tries to get a 10")


def randomRange(n):
    """
    Roll numbers 1–100 n times and print highest and lowest.
    """
    if n <= 0:
        return
    highest = 1
    lowest = 100
    for _ in range(n):
        roll = random.randint(1, 100)
        print(roll)
        if roll > highest:
            highest = roll
        if roll < lowest:
            lowest = roll
    print(f"highest: {highest}")
    print(f"lowest: {lowest}")


def reverse(word: str) -> str:
    """
    Return the reverse of a string.
    """
    result = ""
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
    return result


def fizzBuzzContinuous(n):
    """
    Perform fizzbuzz from 1 to n.
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return " ".join(result)


def collatz(n):
    """
    Run the Collatz sequence starting at n.
    """
    if n <= 0:
        return ""
    result = []
    while n != 1:
        result.append(str(n))
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    result.append("1")
    return " ".join(result)


def fibonacci(n):
    """
    Return first n Fibonacci numbers as a string.
    """
    if n <= 0:
        return ""
    if n == 1:
        return "0"

    result = ["0", "1"]
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        result.append(str(b))
    return " ".join(result)


print(fibonacci(300))
