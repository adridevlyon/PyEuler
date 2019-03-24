from helpers.palindrom_helper import PalindromHelper


class Pb4:
    def __str__(self):
        return "Problem 4 : Largest palindrome product"

    '''
    Compute largest palindrome with one factor fixed to max_factor and get the second factor min_factor
    Like that we know that the largest palindrome has both factors between min_factor and max_factor
    Then, compute, with one factor fixed at any value between those two values, the largest palindrome greater than
    the current maximum.
    This will ensure we don't compute too many things and we have the largest palindrome possible 
    '''
    def largest_palindrom_with_factors_at_most(self, max_factor):
        palindrom_helper = PalindromHelper()
        min_factor, current_largest_palindrom = self.__largest_palindrom(palindrom_helper, max_factor, max_factor, 0)
        for factor in range(max_factor-1, min_factor, -1):
            _, current_largest_palindrom = self.__largest_palindrom(palindrom_helper, max_factor, factor, current_largest_palindrom)
        return current_largest_palindrom

    def __largest_palindrom(self, palindrom_helper, max_factor, fixed_factor, current_largest_palindrom):
        for factor in range(max_factor, 0, -1):
            computed = fixed_factor * factor
            if computed <= current_largest_palindrom:
                return -1, current_largest_palindrom
            elif palindrom_helper.is_palindrom(computed):
                return factor, computed
        return -1, current_largest_palindrom
