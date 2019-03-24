import time
from problems.pb1 import Pb1
from problems.pb2 import Pb2
from problems.pb3 import Pb3
from problems.pb4 import Pb4
from problems.pb5 import Pb5
from problems.pb6 import Pb6


class PbRunner:
    def run(self):
        pb, answer = self.run_problem(6)
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
        return pb, answer


if __name__ == '__main__':
    runner = PbRunner()

    print()
    start_time = time.process_time()
    runner.run()
    end_time = time.process_time()
    print("Execution duration: %g ms" % ((end_time - start_time) * 1000))

