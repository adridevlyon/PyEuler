from functools import reduce

from helpers.prime_helper import PrimeHelper


class Pb10:
    def __str__(self):
        return "Problem 10 : Summation of primes"

    def sum_of_primes_below(self, max_value):
        prime_helper = PrimeHelper()
        primes = prime_helper.all_primes_below(max_value)
        return reduce(lambda x, y : x + y, primes)
