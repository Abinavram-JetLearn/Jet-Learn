def sum_of_numbers(n):
    if n == 1:
        return n
    else:
        return  n + sum_of_numbers(n-1)

print(sum_of_numbers(100))

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(5))

def power(x, y):
    if y == 1:
        return x
    elif y == 0:
        return 1
    else:
        return x * power(x, y-1)

print(power(2,0))

def fibonnacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonnacci(n - 1) + fibonnacci(n - 2)

print(fibonnacci(10))

def sum_of_powers(n):
    if n == 1:
        return n
    else:
        return  n**2 + sum_of_numbers(n-1)

print(sum_of_powers(4))