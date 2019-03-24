class Pb3:
    def __str__(self):
        return "Problem 3 : Largest prime factor"

    def largest_prime_factor(self, input_number):
        return self.__largest_prime_factor(input_number, 2)

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
    def __largest_prime_factor(self, input_number, least_factor_possible):
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
                return self.__largest_prime_factor(int(input_number/next_factor), next_factor)
        else:
            # next_factor is greater than input_number, this should never happen if the method has been called
            # as intended
            raise ValueError("next_factor cannot be greater than input_number, "
                             "the method may have been called with wrong arguments")
