from Excercise_1_Fibonacci import fibonacci_number
from Excercise_1_Fibonacci import fibonacci_series_to
from Excercise_1_Fibonacci import fibonacci_series_from_to

def test_fibonacci_number():
    assert fibonacci_number(6) == 5
   
def test_fibonacci_series_to():
    assert fibonacci_series_to(3) == [0, 1, 2]
    

def test_fibonacci_series_from_to():
    assert fibonacci_series_from_to(2, 4) == [1, 1, 2]
