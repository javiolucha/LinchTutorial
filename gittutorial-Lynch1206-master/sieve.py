import numpy as np


# <ASSIGNMENT 1.5: Implement the Sieve of Eratosthenes>
def sieve(upper_limit):
    """
    Return the highest prime number under a given upper limit.

    :upper_limit (Int)
    """

    n = upper_limit
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    Highest_prime_number=[x for x in range(2, n + 1) if IsPrime[x]]

    return max(Highest_prime_number)
    

# <\ASSIGNMENT 1.5>


if __name__ == "__main__":
    upper_limit = input("Upper limit: ")
    print(f"Highest prime below limit: {sieve(int(upper_limit))}")
