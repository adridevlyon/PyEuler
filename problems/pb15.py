class Pb15:
    def __str__(self):
        return "Problem 15 : Lattice paths"

    '''
    In a n by n grid, going from top-left to bottom-right only with "down" and "right" requires a 2n-long path
    with n "right" and n "down".
    Counting all those paths means counting all the different means of placing n "downs" among 2n positions.
    So it will be the binomial coefficient:
    (2.n)
    ( n )
    so
    (n+1)*(n+2)*...*(2*n)
    ---------------------
    1 * 2 * ... * n
    '''
    def count_paths_in_grid(self, grid_size):
        if grid_size == 0:
            return 0
        else:
            numerator = 1
            denominator = 1
            for k in range(1, grid_size + 1):
                numerator *= (grid_size + k)
                denominator *= k
            return int(numerator / denominator)
