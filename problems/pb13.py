from helpers.number_helper import NumberHelper


class Pb13:
    def __str__(self):
        return "Problem 13 : Large sum"

    '''
    The goal is to compute the first 10 digits of the sum of 100 numbers.
    For each index, the sum of the digits at this index is between 0 and 900.
    There is a really light probability that the sum is less than 100.
    So the digits in the index x (starting from the last digit) will have an impact between 1 and 9 on the sum of the
    digits in the index x + 1 and x + 2.
    Thus, the sum of the 10 first digits should have between 10 and 12 digits.
    The "worst case" would be that this sum has 10 digits.
    In this case, the 11th and 12th digits would impact this sum.
    So if we compute the sum of the 12 first digits of each number, we have at least 12 digits.
    So we can take the first 10 digits and this will be the first 10 digits of the whole sum.
    '''
    def compute_10_first_digits(self):
        large_numbers_start = [
            371072875339,
            463769376774,
            743249861995,
            919422133635,
            230675882075,
            892616706966,
            281128798128,
            442742289174,
            474514457360,
            703864861058,
            621764571418,
            649063524627,
            925758677183,
            582035653253,
            801811993848,
            353986643728,
            865155060062,
            716938887077,
            543700705768,
            532826541087,
            361232725250,
            458765761724,
            174237069058,
            811426604180,
            519343254517,
            624672216484,
            157324443869,
            550376875256,
            183363848253,
            803862875928,
            781828337579,
            167263201004,
            484030981290,
            870869875513,
            599594068957,
            697939506796,
            410526847082,
            653786073615,
            358290353174,
            949537597651,
            889028025717,
            252676802760,
            362702185404,
            240744869082,
            914302881971,
            344130655780,
            230530811728,
            114876969321,
            637832994906,
            677201869716,
            955482553002,
            760853271322,
            377742425354,
            237019132757,
            297988602722,
            184957014548,
            382982037830,
            348295438291,
            409579530664,
            297461521855,
            416981162220,
            624679571944,
            231897067725,
            861880882258,
            113067397083,
            829591747671,
            976233310448,
            428462801835,
            551216035469,
            322381957343,
            755061649651,
            621778427521,
            329241857071,
            995186714302,
            732674608005,
            768418225246,
            971426179103,
            877836461827,
            108488025216,
            713296124747,
            621840735723,
            666278919814,
            606618262936,
            857869440895,
            660243964099,
            649139826800,
            167309393198,
            948093772450,
            786391670211,
            153687137119,
            407899231155,
            448899115014,
            415031288803,
            812348806732,
            826165707739,
            229188020587,
            771585425020,
            721078384350,
            208496039801,
            535035342264
        ]
        first_digits_sum = sum(large_numbers_start)
        number_helper = NumberHelper()
        return number_helper.get_first_digits(first_digits_sum, 10)
