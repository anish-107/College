import numpy as np

def trapezoidal_rule(func, a, b, n):
    """
    Approximate the integral of f(x) from a to b using the Trapezoidal Rule.
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    
    result = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return result

def simpson_1_by_3_rule(func, a, b, n):
    """
    Approximate the integral of f(x) from a to b using the Simpson 1/3 Rule.
    """
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 Rule")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)

    result = (h / 3) * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))
    return result