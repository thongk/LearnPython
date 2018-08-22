import timeit

def func(x, y):
    return x**2 + y**2

t_start = timeit.default_timer()
z = func(3523.3241, 34523.4123)
t_end = timeit.default_timer()

cost = t_end - t_start
print('cost:%f' %cost)