def fibonacci_number(n):
    """This function calculates the "n" number of the fibonacci series
        Args:
            n (int): The number of the fibonacci series required
        Returns:
            int: the number "n" of the fibonacci series
    """
    l = [0, 1] 
    for i in range(n - 1):
        l = [*l, l[-1] + l[-2]]
    return l[n - 1]
   
def fibonacci_series_to(n):
    """This function calculates the fibonacci series until the "n"th element
        Args:
            n (int): The last element of the fibonacci series required
        Returns:
            list: the fibonacci series until the "n"th element
    """
    l = [0, 1] 
    for i in range(n - 1):
        l = [*l, l[-1] + l[-2]]
    return l[:n]

def fibonacci_series_from_to(m, n):
    """This function calculates the fibonacci series from the "m"th 
        element until the "n"th element
        Args:
            m (int): The first element of the fibonacci series required
            n (int): The last element of the fibonacci series required
        Returns:
            list: the fibonacci series from the "n"th element until the "n"th 
            element
    """
    l = [0, 1] 
    for i in range(n - 1):
        l = [*l, l[-1] + l[-2]]
    return l[m - 1:n]

x = 10
y = 20
print('The ' + str(x) + 'th element of the Fibonacci series is: ' + str(fibonacci_number(x)))
print('The Fibonacci series until the ' + str(x) + 'element is: ' + str(fibonacci_series_to(x)))
print('The Fibonacci series from the ' + str(x) + 'th element until the ' + str(y) + 'th element is: ' + str(fibonacci_series_from_to(x, y)))
