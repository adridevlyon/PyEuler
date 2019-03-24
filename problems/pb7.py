class Pb7:
    def __str__(self):
        return "Problem 7 : nth prime"

    def n_th_prime(self, number):
        number_primes = 0
        primes = []
        current_number = 2
        while number_primes < number:
            is_prime = True
            for prime in primes:
                if current_number % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                primes += [current_number]
                number_primes += 1
            current_number += 1

        return current_number - 1
