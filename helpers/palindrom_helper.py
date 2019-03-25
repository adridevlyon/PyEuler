from helpers.number_helper import NumberHelper


class PalindromHelper:

    def is_palindrom(self, number):
        number_helper = NumberHelper()
        number_digits = number_helper.number_digits(number)
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
