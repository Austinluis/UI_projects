def factorial(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return (n * factorial(n - 1))
        
print(factorial(5))