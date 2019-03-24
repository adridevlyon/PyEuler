class Pb2:
    def __str__(self):
        return "Problem 2 : Even Fibonacci numbers"

    def get_sum_of_even_terms_less_than(self, term_ceiling):
        even_sum = 0
        fibo_n = 0
        fibo_n1 = 1
        while fibo_n1 < term_ceiling:
            if fibo_n1 % 2 == 0:
                even_sum += fibo_n1
            fibo_n, fibo_n1 = self.__get_fibo_next(fibo_n, fibo_n1)
        return even_sum

    def __get_fibo_next(self, fibo_n, fibo_n1):
        return fibo_n1, fibo_n + fibo_n1
