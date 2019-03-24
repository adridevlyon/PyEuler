from helpers.prime_helper import PrimeHelper


class Pb3:
    def __str__(self):
        return "Problem 3 : Largest prime factor"

    def largest_prime_factor(self, input_number):
        prime_helper = PrimeHelper()
        return prime_helper.largest_prime_factor(input_number, 2)
