import math


def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False
    
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True


def prime_factorise(n: int) -> [int]:
    factors = []
    if n % 2 == 0:
        factors.append(2)
    
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            if is_prime(x):
                factors.append(x)

    return factors


def factorise(n: int) -> [int]:
    factors = [1, n]

    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            factors.append(x)
            y = int(n / x)
            if x != y:
                factors.append(y)

    return factors

