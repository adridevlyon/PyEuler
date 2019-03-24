from functools import reduce


class Pb5:
    def __str__(self):
        return "Problem 5 : Smallest multiple"

    def smallest_common_multiple_for_all_numbers_below(self, maximum_value):
        smallest_common_factors = []
        for value in range(2, maximum_value + 1):
            factors = self.__factors(value, [], 2)
            smallest_common_factors = self.__merge_factors(smallest_common_factors, factors)
        return reduce((lambda x, y : x * y), [pow(ind, val) for ind, val in enumerate(smallest_common_factors)])

    def __factors(self, input_number, factors, least_factor_possible):
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
                return self.__factors(int(input_number/next_factor), self.__add_factor(factors, next_factor), next_factor)
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

    def __merge_factors(self, factors_1, factors_2):
        merged_factors = [0] * max(len(factors_1), len(factors_2))
        self.__max__by_index(merged_factors, factors_1)
        self.__max__by_index(merged_factors, factors_2)
        return merged_factors

    def __max__by_index(self, all_factors, factors):
        for ind, val in enumerate(factors):
            all_factors[ind] = max(all_factors[ind], val)
