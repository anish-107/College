import numpy as np
import matplotlib.pyplot as plt

def plot_trapezoidal(func, a, b, n):
    x = np.linspace(a, b, 400)
    y = func(x)

    xi = np.linspace(a, b, n + 1)
    yi = func(xi)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, 'b', linewidth=2, label='f(x)')

    # Draw trapezoids with shading
    for i in range(n):
        xs = [xi[i], xi[i], xi[i+1], xi[i+1]]
        ys = [0, yi[i], yi[i+1], 0]
        ax.fill(xs, ys, color='orange', alpha=0.4, edgecolor='r')

    ax.scatter(xi, yi, color="red", zorder=5, label="Sample points")

    ax.set_title(f"Trapezoidal Rule Approximation (n={n})", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)

    return fig


def plot_simpson_1_by_3(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 Rule")

    x = np.linspace(a, b, 400)
    y = func(x)

    xi = np.linspace(a, b, n + 1)
    yi = func(xi)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, 'b', linewidth=2, label='f(x)')

    # Draw Simpson parabolas (every 2 subintervals)
    for i in range(0, n, 2):
        xs = np.linspace(xi[i], xi[i+2], 100)
        p = np.polyfit([xi[i], xi[i+1], xi[i+2]],
                       [yi[i], yi[i+1], yi[i+2]], 2)
        ys = np.polyval(p, xs)
        ax.fill_between(xs, ys, alpha=0.3, color="orange")
        ax.plot(xs, ys, 'r--', linewidth=1.5, label="Parabola" if i == 0 else "")

    ax.scatter(xi, yi, color="red", s=40, zorder=5, label="Sample points")

    ax.set_title(f"Simpson's 1/3 Rule Approximation (n={n})", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)

    return fig
