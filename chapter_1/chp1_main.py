from imports import *

def fib_recur(n: int) -> int:
    #Simple recursive function for finding fib numbers
    if n <= 2:
        return n
    return fib_recur(n-1) + fib_recur(n-2)


#write function to get minimum value in list


