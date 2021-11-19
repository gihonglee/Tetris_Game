import numpy as np
import math

a = [116,78,36,145,39,44,48,60,34,15]

def mean(a):
    result = 0
    for i in a:
        result += i
    return result / len(a)

def std(a):
    result = 0
    for i in a:
        result += (i - mean(a))**2
    return math.sqrt(result / (len(a)-1))

print(mean(a))
print(std(a))