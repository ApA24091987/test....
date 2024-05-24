def test_(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} = {value}')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


test_(1, 3, 5, a=7, b=8, c=9)
print(factorial(5))
