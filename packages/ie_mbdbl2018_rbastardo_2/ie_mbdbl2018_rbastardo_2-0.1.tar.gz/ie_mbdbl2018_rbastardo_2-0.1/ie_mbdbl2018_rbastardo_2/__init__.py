# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:45:16 2018

@author: Rafael Bastardo
"""
def linear_congruences_random_generator(X0=3,a=22695477,b=1,m=2**32,throws=1):
    """Function generates a list of random numbers using linear congruences equation X1=(a*X0+b) mod(m)
    Default values: a=22695477,b=1,m=2**32 and X0=3, throws=1"""
    if is_int(X0) == True and is_int(a) == True and is_int(b) == True and is_int(m) == True and is_int(m) == True and m>1:
        random=list()
        for i in range(1,throws+1):
            x=(a*X0+b)%m
            random.insert(i,x)
            X0=x
        return(random)
    else: 
        print("All arguments must be positive integers and m greater than 1")
    return

# function that verifies the input is an integer needed to run linear_congruences_random_generator() function
def is_int(value):
    """Function to verify the input is an integer"""
    try:
        value = int(value)
        if value<0:
                print("Please enter a positive integer greater than 0")
                return (False)
        return (True)
    except ValueError:
        print("The input is not an integer!!!")
        return (False)
