#!/bin/python

import math
# Complete the solve function below.
t = int(input())

while t > 0:
    n = int(input())
    k = int(input())
    print math.factorial(n + k - 1) / (math.factorial(k) * math.factorial(n - 1)) % 1000000000
    t = t - 1
