import numpy as np

def roots(f, a, b, tol=1e-10, max_iter=1000):
    #Check if the function values at a and b have opposite signs
    if f(a)*f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    for i in range(max_iter):
        c = (a+b)/2
        if abs(f(c)) < tol: #If f(c) is close enough to 0
            return round(c, 10)

        if f(a)*f(c) < 0: #Root is in [a, c]
            b = c
        else: #Root is in [c, b]
            a = c

    raise ValueError("Maximum iterations exceeded.")

#Test cases
#1. f(x) = e^x + ln(x) on [0, 1]
def f1(x):
    return np.exp(x) + np.log(x)

#2. f(x) = arctan(x) - x^2 on [0, 2]
def f2(x):
    return np.arctan(x) - x**2

#3. f(x) = sin(x) - ln(x) on [3, 4]
def f3(x):
    return np.sin(x) - np.log(x)

#4. f(x) = ln(cos(x)) on [5, 7]
def f4(x):
    return np.log(np.cos(x))

#Running the tests
try:
    root1 = roots(f1, 0.001, 1) #Start just above 0 to avoid log(0)
    print(f"Root of f1: {root1}")
except ValueError as e:
    print(e)

try:
    root2 = roots(f2, 0, 2)
    print(f"Root of f2: {root2}")
except ValueError as e:
    print(e)

try:
    root3 = roots(f3, 3, 4)
    print(f"Root of f3: {root3}")
except ValueError as e:
    print(e)

try:
    root4 = roots(f4, 5, 7)
    print(f"Root of f4: {root4}")
except ValueError as e:
    print(e)