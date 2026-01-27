"""
prime.py -- Write the application code here
"""

def generate_prime_factors(num):
    if type(num) is not int:
        raise ValueError("Input must be an integer")
    if num == 1:
        return []