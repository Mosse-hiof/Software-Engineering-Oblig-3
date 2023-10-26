from leap_year import is_a_leap_year


# Checks if leap year
def test_if_year_divisible_by_400_is_a_leap_year():
    assert is_a_leap_year(1600) == (1600 % 400 == 0)
    assert not is_a_leap_year(1724) == (1724 % 400 == 0)
    assert not is_a_leap_year(1844) == (1844 % 400 == 0)
    assert not is_a_leap_year(1896) == (1896 % 400 == 0)
    assert not is_a_leap_year(1960) == (1960 % 400 == 0)


def test_if_year_divisible_by_4_but_not_100_is_a_leap_year():
    assert not (1600 % 4 == 0 and 1600 % 100 != 0) == is_a_leap_year(1600)
    assert is_a_leap_year(1724) == (1724 % 4 == 0 and 1724 % 100 != 0)
    assert is_a_leap_year(1844) == (1844 % 4 == 0 and 1844 % 100 != 0)
    assert is_a_leap_year(1896) == (1896 % 4 == 0 and 1896 % 100 != 0)
    assert is_a_leap_year(1960) == (1960 % 4 == 0 and 1960 % 100 != 0)


# Checks if not leap year
def test_if_year_not_divisible_by_4_is_not_a_leap_year():
    assert is_a_leap_year(1700) == (1700 % 4 != 0)
    assert is_a_leap_year(1800) == (1800 % 4 != 0)
    assert is_a_leap_year(1900) == (1900 % 4 != 0)
    assert is_a_leap_year(2600) == (2600 % 4 != 0)


def test_if_year_divisible_by_100_but_not_400_is_not_a_leap_year():
    assert not is_a_leap_year(1700) == (1700 % 100 == 0 and 1700 % 400 != 0)
    assert not is_a_leap_year(1800) == (1800 % 100 == 0 and 1800 % 400 != 0)
    assert not is_a_leap_year(1900) == (1900 % 100 == 0 and 1900 % 400 != 0)
    assert not is_a_leap_year(2600) == (2600 % 100 == 0 and 2600 % 400 != 0)
