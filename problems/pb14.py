class Pb14:
    def __str__(self):
        return "Problem 14 : Longest Collatz sequence"

    def collatz_sequence_length(self, start_number):
        return self.__collatz_sequence_length_optimized(start_number, {1: 1})

    def __next_element(self, number):
        return int(number / 2) if number % 2 == 0 else int(3 * number + 1)

    def longest_collatz_sequence(self, max_start):
        index, max_len, known_collatz = self.__compute_collatz_sequence_length_for_powers_of_2(max_start)

        # if n is even, length is 1 + length for n/2
        # so if 2n <= max_start, length for 2n > length for n
        # thus the longest sequence is for a seed > max_start/2
        for start in range(int(max_start / 2) + 1, max_start + 1):
            if known_collatz.get(start) is None:
                length = self.__collatz_sequence_length_optimized(start, known_collatz)
                if length > max_len:
                    index, max_len = start, length
        return index

    def __collatz_sequence_length_optimized(self, start, known_collatz):
        length = known_collatz.get(start)
        if length is not None:
            # length is already known so avoid computing it again
            return length
        else:
            if start % 2 == 0:
                # if n is even, length is 1 + length for n/2
                length = 1 + self.__collatz_sequence_length_optimized(self.__next_element(start), known_collatz)
            else:
                # if n is odd, length is 1 + length for 3*n + 1, that is even, so 2 + length for (3n + 1)/2
                length = 2 + self.__collatz_sequence_length_optimized(int(self.__next_element(start) / 2), known_collatz)
            # store every computed length to avoid recomputing it later
            known_collatz[start] = length
            return length

    '''
    If n is even, length is 1 + length for n/2
    So length for 2^(k + 1) = 1 + length for 2^k = ... = k + 1
    '''
    def __compute_collatz_sequence_length_for_powers_of_2(self, max_start):
        known_collatz = {}
        start = 1
        length = 1
        while start <= max_start:
            known_collatz[start] = length
            start *= 2
            length += 1
        return int(start / 2), length - 1, known_collatz
