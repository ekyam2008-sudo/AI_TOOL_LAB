def is_even(n):
    return n % 2 == 0


def factorial(n):
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


print("Is 10 even?", is_even(10))
print("Factorial of 5:", factorial(5))
print("Is 17 prime?", is_prime(17))