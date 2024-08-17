# Recursion Fibonacci 

def fibonacci(n):

# Base Case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
# This uses the fibonacci sequence to calculate to 55. It is not a standard count like 1,2,3,4,5 & so fourth.