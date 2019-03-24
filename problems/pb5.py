from functools import reduce

from helpers.collection_helper import CollectionHelper
from helpers.prime_helper import PrimeHelper


class Pb5:
    def __str__(self):
        return "Problem 5 : Smallest multiple"

    def smallest_common_multiple_for_all_numbers_below(self, maximum_value):
        smallest_common_factors = []
        prime_helper = PrimeHelper()
        collection_helper = CollectionHelper()
        for value in range(2, maximum_value + 1):
            factors = prime_helper.factors(value, [], 2)
            smallest_common_factors = collection_helper.maximum_term_by_term(smallest_common_factors, factors)
        return reduce((lambda x, y : x * y), [pow(ind, val) for ind, val in enumerate(smallest_common_factors)])
