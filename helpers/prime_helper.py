from functools import reduce


class PrimeHelper:

    def all_primes_below(self, max_value):
        eratosthenes_sieve_odds = [True] * (int((max_value - 1) / 2))
        for ind, prime_candidate in enumerate(eratosthenes_sieve_odds):
            if prime_candidate:
                prime_value = 2 * ind + 3
                next_multiple = prime_value * prime_value
                while next_multiple <= max_value:
                    eratosthenes_sieve_odds[int((next_multiple - 3) / 2)] = False
                    next_multiple += 2 * prime_value

        return [2] + [2 * ind + 3 for ind, x in enumerate(eratosthenes_sieve_odds) if x]

    '''
    Here we don't care to check if the factor is a prime number.
    The reason is simple : it is intended to be called a certain way.
    The constraint is to ensure that the least factor of input_number is least_factor_possible
    How did I choose to do that : 
    * start with least_factor_possible = 2
    * when found factor f divides input_number, recursive call with input_number/f
    With that, found factor can't be composite because its prime factors have been already added to the factors
    and "removed" from input_number by the previous calls
    '''
    def factors(self, input_number, factors, least_factor_possible):
        next_factor = least_factor_possible
        is_divisible = input_number % next_factor == 0
        while not is_divisible \
                and next_factor <= input_number: # this check to avoid an infinite loop that proper calls cannot cause
            next_factor += 1
            is_divisible = input_number % next_factor == 0

        if is_divisible:
            # next_factor divides input_number
            if input_number == next_factor:
                # input_number is next_factor so this is the largest prime factor
                return self.__add_factor(factors, next_factor)
            else:
                # else divide input_number by it and continue with next_factor as least possible
                return self.factors(int(input_number/next_factor), self.__add_factor(factors, next_factor), next_factor)
        else:
            # next_factor is greater than input_number, this should never happen if the method has been called
            # as intended
            raise ValueError("next_factor cannot be greater than input_number, "
                             "the method may have been called with wrong arguments")

    def __add_factor(self, factors, factor):
        if len(factors) < factor + 1:
            factors += ([0] * (factor + 1 - len(factors)))
        factors[factor] += 1
        return factors

    '''
    Here we don't care to check if the factor is a prime number.
    The reason is simple : it is intended to be called a certain way.
    The constraint is to ensure that the least factor of input_number is least_factor_possible
    How did I choose to do that : 
    * start with least_factor_possible = 2
    * when found factor f divides input_number, recursive call with input_number/f
    With that, found factor can't be composite because its prime factors have been "removed" from input_number 
    by the previous calls
    '''
    def largest_prime_factor(self, input_number, least_factor_possible):
        next_factor = least_factor_possible
        is_divisible = input_number % next_factor == 0
        while not is_divisible \
                and next_factor <= input_number: # this check to avoid an infinite loop that proper calls cannot cause
            next_factor += 1
            is_divisible = input_number % next_factor == 0

        if is_divisible:
            # next_factor divides input_number
            if input_number == next_factor:
                # input_number is next_factor so this is the largest prime factor
                return input_number
            else:
                # else divide input_number by it and continue with next_factor as least possible
                return self.largest_prime_factor(int(input_number / next_factor), next_factor)
        else:
            # next_factor is greater than input_number, this should never happen if the method has been called
            # as intended
            raise ValueError("next_factor cannot be greater than input_number, "
                             "the method may have been called with wrong arguments")

    def number_divisors(self, factors):
        return reduce(lambda x, y : x * y, [f + 1 for f in factors])
