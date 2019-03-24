class Pb9:
    def __str__(self):
        return "Problem 9 : Special Pythagorean triplet"

    def product_of_pythagorean_triplet(self, sum_of_triplet):
        for a in range(1, sum_of_triplet - 1):
            for b in range(1, a + 1):
                c = sum_of_triplet - a - b
                if a * a + b * b == c * c:
                    return a * b * c

        return -1
