from helpers.prime_helper import PrimeHelper


class Pb12:
    def __str__(self):
        return "Problem 12 : Highly divisible triangular number"

    def first_triangle_number_with_n_divisors(self, min_divisors_number):
        prime_helper = PrimeHelper()
        current_index = 1
        triangle_number = 1
        nb_divisors = 1
        while nb_divisors < min_divisors_number:
            current_index += 1
            triangle_number += current_index
            factors = prime_helper.factors(triangle_number, [], 2)
            nb_divisors = prime_helper.number_divisors(factors)

        return triangle_number
