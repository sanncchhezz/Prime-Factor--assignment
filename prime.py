"""
prime.py -- Write the application code here
"""

def generate_prime_factors(num):
    """ This function generates prime factors for a given number """
    if type(num) is not int:
        raise ValueError("Input must be an integer")
    if num == 1:
        return []
    if num == 2:
        return [2]
  
    