# -*- coding: utf-8 -*-
"""
Created on Fri May  8 8:16:55 2020

@author: Carlo
"""

from test_Excercise_1_Fibonacci_1 import fibonacci_number
from test_Excercise_1_Fibonacci_1 import fibonacci_series_to
from test_Excercise_1_Fibonacci_1 import fibonacci_series_from_to


def test_fibonacci_number(n):
    fibonacci_number(6) == 5
   
def test_fibonacci_series_to(n):
    fibonacci_series_to(3) == [0, 1, 1]



def test_fibonacci_series_from_to(m, n):
    fibonacci_series_from_to(2, 4) == [1, 1, 2]