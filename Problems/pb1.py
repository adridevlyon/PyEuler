class Pb1:
    def get_multiples_sum(self, multiples_list, ceiling):
        multiples_sum = 0
        nb_multiples = len(multiples_list)
        for i in range(1, ceiling):
            is_multiple = False
            multiple_index = 0
            while not is_multiple and multiple_index < nb_multiples:
                if i % multiples_list[multiple_index] == 0:
                    multiples_sum += i
                    is_multiple = True
                else:
                    multiple_index += 1

        return multiples_sum

if __name__ == '__main__':
    pb1 = Pb1()
    print(pb1.get_multiples_sum([3, 5], 1000))
