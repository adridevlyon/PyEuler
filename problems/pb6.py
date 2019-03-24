from functools import reduce


class Pb6:
    def __str__(self):
        return "Problem 6 : Sum square difference"

    def difference_squares_and_sum(self, maximum_value):
        sum_all = int(maximum_value * (maximum_value + 1) / 2)
        square_sum = pow(sum_all, 2)
        squares = [x*x for x in range(1, maximum_value + 1)]
        sum_squares = reduce(lambda x, y : x + y, squares)
        return square_sum - sum_squares
