import pytest

from target import (
    is_adult, celsius_to_fahrenheit, count_vowels, invert, greet,
    find_max, get_price, swap, common_items, is_leap_year, to_int,
    divide, power, square_root, factorial, average
)


# 1. is_adult
@pytest.mark.parametrize("age, expected", [
    (18, True), (19, True), (100, True), (17, False), (0, False),
])
def test_is_adult_valid_and_boundaries(age, expected):
    assert is_adult(age) is expected

@pytest.mark.parametrize("age", [-1, -100])
def test_is_adult_negative_age(age):
    with pytest.raises(ValueError, match="age cannot be negative"):
        is_adult(age)

def test_is_adult_wrong_type():
    with pytest.raises(TypeError):
        is_adult("18")


# 2. celsius_to_fahrenheit
@pytest.mark.parametrize("celsius, expected", [
    (0, 32.0), (100, 212.0), (-40, -40.0), (25, 77.0),
    (37, 98.6), (0.5, 32.9),
])
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == expected

def test_celsius_to_fahrenheit_wrong_type():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("0")


# 3. count_vowels
@pytest.mark.parametrize("text, expected", [
    ("Hello", 2), ("EDUCATION", 5), ("Python", 1),
    ("xyz", 0), ("", 0), ("AEIOUaeiou", 10),
])
def test_count_vowels_valid(text, expected):
    assert count_vowels(text) == expected

@pytest.mark.parametrize("value", [123, None, ["hello"]])
def test_count_vowels_wrong_type(value):
    with pytest.raises(TypeError, match="text must be a string"):
        count_vowels(value)


# 4. invert
@pytest.mark.parametrize("flag, expected", [(True, False), (False, True)])
def test_invert_valid(flag, expected):
    assert invert(flag) is expected

@pytest.mark.parametrize("value", [1, 0, "True", None])
def test_invert_wrong_type(value):
    with pytest.raises(TypeError, match="flag must be True or False"):
        invert(value)


# 5. greet
@pytest.mark.parametrize("name, expected", [
    (None, "Hello, Guest!"), ("", "Hello, Guest!"),
    ("   ", "Hello, Guest!"), ("Bappy", "Hello, Bappy!"),
    ("  Karim  ", "Hello, Karim!"),
])
def test_greet(name, expected):
    assert greet(name) == expected

def test_greet_wrong_type():
    with pytest.raises(AttributeError):
        greet(123)


# 6. find_max
@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 3), ([-10, -5, -20], -5),
    ([7], 7), ([0, 0], 0),
])
def test_find_max_valid(numbers, expected):
    assert find_max(numbers) == expected

def test_find_max_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        find_max([])

def test_find_max_wrong_type():
    with pytest.raises(TypeError):
        find_max(123)

def test_find_max_incomparable_values():
    with pytest.raises(TypeError):
        find_max([1, "two"])


# 7. get_price
@pytest.mark.parametrize("item, expected", [("apple", 10), ("banana", 20)])
def test_get_price_existing_item(item, expected):
    prices = {"apple": 10, "banana": 20}
    assert get_price(prices, item) == expected

def test_get_price_missing_item():
    with pytest.raises(KeyError, match="orange not found"):
        get_price({"apple": 10}, "orange")

def test_get_price_unhashable_item():
    with pytest.raises(TypeError):
        get_price({"apple": 10}, ["apple"])


# 8. swap
@pytest.mark.parametrize("pair, expected", [
    ((1, 2), (2, 1)), (("A", "B"), ("B", "A")),
    ((None, 0), (0, None)),
])
def test_swap_valid(pair, expected):
    result = swap(pair)
    assert result == expected
    assert isinstance(result, tuple)

@pytest.mark.parametrize("pair", [(), (1,), (1, 2, 3)])
def test_swap_wrong_length(pair):
    with pytest.raises(ValueError, match="pair must have exactly 2 values"):
        swap(pair)

def test_swap_wrong_type():
    with pytest.raises(TypeError):
        swap(123)


# 9. common_items
@pytest.mark.parametrize("set_a, set_b, expected", [
    ({1, 2, 3}, {2, 3, 4}, {2, 3}),
    ({1, 2}, {3, 4}, set()),
    ({1}, {1}, {1}),
    (set(), {1, 2}, set()),
])
def test_common_items(set_a, set_b, expected):
    result = common_items(set_a, set_b)
    assert result == expected
    assert isinstance(result, set)

def test_common_items_wrong_type():
    with pytest.raises(TypeError):
        common_items({1, 2}, [2])


# 10. is_leap_year
@pytest.mark.parametrize("year, expected", [
    (2024, True), (2025, False), (1900, False),
    (2000, True), (2028, True), (4, True), (1, False),
])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) is expected

@pytest.mark.parametrize("year", [0, -1, -100])
def test_is_leap_year_invalid_year(year):
    with pytest.raises(ValueError, match="year must be 1 or more"):
        is_leap_year(year)

def test_is_leap_year_wrong_type():
    with pytest.raises(TypeError):
        is_leap_year("2024")


# 11. to_int
@pytest.mark.parametrize("value, expected", [
    ("100", 100), (25.8, 25), (0, 0), ("-12", -12),
])
def test_to_int_valid(value, expected):
    result = to_int(value)
    assert result == expected
    assert isinstance(result, int)

@pytest.mark.parametrize("value", [True, False])
def test_to_int_rejects_bool(value):
    with pytest.raises(TypeError, match="bool is not allowed"):
        to_int(value)

def test_to_int_invalid_string():
    with pytest.raises(ValueError):
        to_int("abc")

def test_to_int_wrong_type():
    with pytest.raises(TypeError):
        to_int(object())


# 12. divide
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0), (20, 4, 5.0), (-10, 2, -5.0),
    (0, 5, 0.0), (7, 2, 3.5),
])
def test_divide_valid(a, b, expected):
    result = divide(a, b)
    assert result == expected
    assert isinstance(result, float)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        divide(10, 0)

def test_divide_wrong_type():
    with pytest.raises(TypeError):
        divide("10", 2)


# 13. power
@pytest.mark.parametrize("base, exponent, expected", [
    (2, 3, 8), (5, 2, 25), (10, 0, 1),
    (2, -1, 0.5), (3, 3, 27), (0, 3, 0),
])
def test_power_valid(base, exponent, expected):
    assert power(base, exponent) == expected

def test_power_wrong_type():
    with pytest.raises(TypeError):
        power(2, "3")


# 14. square_root
@pytest.mark.parametrize("value, expected", [
    (25, 5.0), (16, 4.0), (0, 0.0), (1, 1.0),
])
def test_square_root_exact(value, expected):
    result = square_root(value)
    assert result == expected
    assert isinstance(result, float)

def test_square_root_inexact():
    assert square_root(2) == pytest.approx(2 ** 0.5)

def test_square_root_negative():
    with pytest.raises(ValueError, match="cannot take the square root of a negative number"):
        square_root(-4)

def test_square_root_wrong_type():
    with pytest.raises(TypeError):
        square_root("4")


# 15. factorial
@pytest.mark.parametrize("n, expected", [
    (0, 1), (1, 1), (3, 6), (5, 120), (10, 3628800),
])
def test_factorial_valid(n, expected):
    result = factorial(n)
    assert result == expected
    assert isinstance(result, int)

def test_factorial_negative():
    with pytest.raises(ValueError, match="factorial is not defined for negative numbers"):
        factorial(-1)

def test_factorial_wrong_type():
    with pytest.raises(TypeError):
        factorial(2.5)


# 16. average
@pytest.mark.parametrize("numbers, expected", [
    ([10, 20, 30], 20.0), ([5, 5, 5], 5.0),
    ([1, 2], 1.5), ([-10, 10], 0.0), ([7], 7.0),
])
def test_average_valid(numbers, expected):
    result = average(numbers)
    assert result == expected
    assert isinstance(result, float)

def test_average_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        average([])

def test_average_wrong_type():
    with pytest.raises(TypeError):
        average("123")
