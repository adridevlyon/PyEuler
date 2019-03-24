import time
from problems.pb1 import Pb1
from problems.pb10 import Pb10
from problems.pb11 import Pb11
from problems.pb2 import Pb2
from problems.pb3 import Pb3
from problems.pb4 import Pb4
from problems.pb5 import Pb5
from problems.pb6 import Pb6
from problems.pb7 import Pb7
from problems.pb8 import Pb8
from problems.pb9 import Pb9


class PbRunner:
    def run(self):
        pb, answer = self.run_problem(11)
        if pb != None:
            print(pb)
            print("Answer:", answer)
        else:
            print("Not implemented yed!")

    def run_problem(self, pb_number):
        pb = None
        answer = None
        if pb_number == 1:
            pb = Pb1()
            answer = pb.get_multiples_sum([3, 5], 1000)
        elif pb_number == 2:
            pb = Pb2()
            answer = pb.get_sum_of_even_terms_less_than(4000000)
        elif pb_number == 3:
            pb = Pb3()
            answer = pb.largest_prime_factor(600851475143)
        elif pb_number == 4:
            pb = Pb4()
            answer = pb.largest_palindrom_with_factors_at_most(999)
        elif pb_number == 5:
            pb = Pb5()
            answer = pb.smallest_common_multiple_for_all_numbers_below(20)
        elif pb_number == 6:
            pb = Pb6()
            answer = pb.difference_squares_and_sum(100)
        elif pb_number == 7:
            pb = Pb7()
            answer = pb.n_th_prime(10001)
        elif pb_number == 8:
            pb = Pb8()
            answer = pb.greatest_product(13)
        elif pb_number == 9:
            pb = Pb9()
            answer = pb.product_of_pythagorean_triplet(1000)
        elif pb_number == 10:
            pb = Pb10()
            answer = pb.sum_of_primes_below(2000000)
        elif pb_number == 11:
            pb = Pb11()
            answer = pb.greatest_product(4)
        return pb, answer


if __name__ == '__main__':
    runner = PbRunner()

    print()
    start_time = time.process_time()
    runner.run()
    end_time = time.process_time()
    print("Execution duration: %g ms" % ((end_time - start_time) * 1000))

