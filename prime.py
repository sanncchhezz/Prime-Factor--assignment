"""
prime.py -- Write the application code here
"""

def generate_prime_factors(num):
    """ This function generates prime factors for a given number """
    prime_factors = []
    first_prime = 2
    
    if type(num) is not int:
        raise ValueError("Input must be an integer")
    
    if num == 1:
        return prime_factors   

    while num > 1:
        if num % first_prime == 0:
            prime_factors.append(first_prime)
            num = num // first_prime # Use integer division to avoid float results
        else:
            first_prime += 1
   
    return prime_factors




  
    