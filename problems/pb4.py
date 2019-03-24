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
        min_factor, current_largest_palindrome = self.__largest_palindrom(max_factor, max_factor, 0)
        for factor in range(max_factor-1, min_factor, -1):
            _, current_largest_palindrome = self.__largest_palindrom(max_factor, factor, current_largest_palindrome)
        return current_largest_palindrome

    def __largest_palindrom(self, max_factor, fixed_factor, current_largest_palindrome):
        for factor in range(max_factor, 0, -1):
            computed = fixed_factor * factor
            if computed <= current_largest_palindrome:
                return -1, current_largest_palindrome
            elif self.__is_palindrome(computed):
                return factor, computed
        return -1, current_largest_palindrome

    def __is_palindrome(self, number):
        number_digits = self.__number_digits(number)
        power_10_last_digit = 1
        power_10_first_digit = pow(10, number_digits - 1)
        for index_digit in range(0, number_digits):
            first_digit = int(number / power_10_first_digit) % 10
            last_digit = int(number % (10 * power_10_last_digit) / power_10_last_digit)
            if first_digit != last_digit:
                return False
            power_10_last_digit *= 10
            power_10_first_digit = int(power_10_first_digit / 10)
        return True

    def __number_digits(self, number):
        number_digits = 1
        power_10 = 10
        while power_10 < number:
            number_digits += 1
            power_10 *= 10
        return number_digits
