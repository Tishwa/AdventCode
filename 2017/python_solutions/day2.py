def format_input(x):
    """Transforms rows of numers written as strings into a list of lists of ints"""
    delimiter = '\t' if '\t' in x else ' ' # test_value doesn't use \t but input does
    return [[int(s) for s in r.split(delimiter) if s != ''] for r in x.split('\n')]

def get_diff(r):
    """Given a list of ints r, returns the difference between its max and min"""
    return max(r) - min(r)

def solve_1(x):
    """Returns the checksum (sum of the difference between the biggest and smallest number in each row)"""
    return sum(map(get_diff, format_input(x)))

def get_even_div(r):
    """Given a list of ints r, returns the first even result of a division between two of its numbers"""
    for i in range(len(r)):
        for j in range(i+1, len(r)):
            if r[i] % r[j] == 0:
                return r[i] // r[j]
            if r[j] % r[i] == 0:
                return r[j] // r[i]
    return 0

def solve_2(x):
    """Returns the sum of the evenly divisble values for each of the given rows"""
    return sum(map(get_even_div, format_input(x)))
