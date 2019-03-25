class NumberHelper:

    def number_digits(self, number):
        number_digits = 1
        power_10 = 10
        while power_10 < number:
            number_digits += 1
            power_10 *= 10
        return number_digits

    def get_first_digits(self, number, number_digits_to_take):
        number_digits = self.number_digits(number)
        if number_digits <= number_digits_to_take:
            return number
        else:
            return int(number / pow(10, number_digits - number_digits_to_take))
