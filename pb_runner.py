import time
from problems.pb1 import Pb1


class PbRunner:
    def run(self):
        pb, answer = self.run_problem(1)
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
        return pb, answer


if __name__ == '__main__':
    runner = PbRunner()

    print()
    start_time = time.process_time_ns()
    runner.run()
    end_time = time.process_time_ns()
    print("Execution duration: %g ns" % (end_time - start_time))

