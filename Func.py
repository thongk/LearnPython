import math

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-9999))

def power(x ,n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(8))


