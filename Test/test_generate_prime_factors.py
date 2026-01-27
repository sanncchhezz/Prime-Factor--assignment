import prime
import pytest

def test_prime_number_ValueError():
    """ tests for ValueError when input is not an integer """
    with pytest.raises(ValueError):
        assert prime.generate_prime_factors("hello")


def test_prime_number_returns_empty_list():
    """ tests for an empty list when input is 1 """
    assert prime.generate_prime_factors(1) == []

def test_prime_number_returns_two_in_list():
    """ tests for a list with 2 when input is 2 """
    assert prime.generate_prime_factors(2) == [2]

def test_prime_number_returns_three_in_list():
    """ tests for a list with 3 when input is 3 """
    assert prime.generate_prime_factors(3) == [3]

def test_prime_number_returns_multiple_products():
    """ tests for a list with multiple prime factors """
    assert prime.generate_prime_factors(4) == [2, 2]
