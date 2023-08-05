def are_numbers_equal(number1, number2, allowed_difference=10**1):
    return abs(number1 - number2) < allowed_difference


def are_numbers_equal_diff_0_1(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**-0)


def are_numbers_equal_diff_0_01(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**-1)


def are_numbers_equal_diff_0_001(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**-2)


def are_numbers_equal_diff_0_0001(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**-3)


def are_numbers_equal_diff_0_00001(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**-4)


def are_numbers_equal_diff_0_000001(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**-5)


def are_numbers_equal_diff_0_0000001(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**-6)


def are_numbers_equal_diff_0_00000001(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**-7)


def are_numbers_equal_diff_10(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**1)


def are_numbers_equal_diff_100(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**2)


def are_numbers_equal_diff_1000(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**3)


def are_numbers_equal_diff_10000(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**4)


def are_numbers_equal_diff_100000(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**5)


def are_numbers_equal_diff_1000000(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**6)


def are_numbers_equal_diff_10000000(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**7)


def are_numbers_equal_diff_100000000(number1, number2):
    return are_numbers_equal(number1, number2, allowed_difference=10**8)


