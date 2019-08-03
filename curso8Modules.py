from math import sqrt
from math import trunc
import random

n = random.randint(1, 99999)
print('Squad of {} is {}.'.format(n, trunc(sqrt(n))))
