import prime
import pytest

def test_prime_number_ValueError():
    """ tests for ValueError when input is not an integer """
    with pytest.raises(ValueError):
        assert prime.generate_prime_factors("hello")

