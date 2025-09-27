import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi


a = 0  # lower limit
b = 2  # upper limit

# Define the function and the limits of integration
def f(x):
    return (np.abs(np.sin(5*x)*np.sin(11*x)) + 0.1) * (1 + 0.4*np.exp(-6*(x - 1)**2))

def monte_carlo_integration_mean(a: float, b: float, f: callable, n: int) -> float:
    '''
    Function to estimate the integral of f(x) from a to b using the Monte Carlo method.
        Args:
            a: float, lower limit of integration
            b: float, upper limit of integration
            f: callable, the function to integrate
            n: int, number of random samples to use
        Returns:
            float, the estimated value of the integral
    '''
    if n <= 0:
        raise ValueError("n must be positive")
    rng = np.random.default_rng(42)
    total = 0
    for _ in range(n):
        x = rng.uniform(a, b)
        total += f(x)
    return (b - a) * total / n

def monte_carlo_integration_area(a: float, b: float, h: float, f: callable, n: int) -> float:
    '''
    Function to estimate the integral of f(x) from a to b using the Monte Carlo method
    by sampling points in the rectangle defined by (a,0), (b,0), (b,h), (a,h).
        Args:
            a: float, lower limit of integration
            b: float, upper limit of integration
            h: float, height of the rectangle (must be >= max(f(x)) for x in [a,b])
            f: callable, the function to integrate
            n: int, number of random samples to use
        Returns:
            float, the estimated value of the integral'''
    if n <= 0:
        raise ValueError("n must be positive")
    random.seed(42)
    rect_area = (b - a) * h
    avg = 0.0
    for __ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0.0, h)
        if y <= f(x):
            avg += 1
    return (avg / n) * rect_area

def draw_function(a: float, b: float, f: callable) -> None:
    '''
    Function to plot f(x) and shade the area under the curve from a to b.
        Args:
            a: float, lower limit of integration
            b: float, upper limit of integration
    '''
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Add vertical dashed lines at the integration limits
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Graph of f(x) from ' + str(a) + ' to ' + str(b))
    plt.grid()
    plt.show()

if __name__ == "__main__":
    draw_function(a, b, f)
    print("-" * 40)
    result, error = spi.quad(f, a, b, epsabs=1e-10, epsrel=1e-10, limit=200)
    print(f"Scipy integrate f(x) from {a} to {b}:  \033[92m{result:.6f}\033[0m")
    n=10000
    print(f"Monte Carlo mean N \033[92m{n}\033[0m   integrate f(x) from {a} to {b}: \033[92m{monte_carlo_integration_mean(a, b, f, n):.6f}\033[0m")
    print(f"Monte Carlo area N \033[92m{n}\033[0m   integrate f(x) from {a} to {b}: \033[92m{monte_carlo_integration_area(a, b, 1.6, f, n):.6f}\033[0m")
    n=100000
    print(f"Monte Carlo mean N \033[92m{n}\033[0m  integrate f(x) from {a} to {b}: \033[92m{monte_carlo_integration_mean(a, b, f, n):.6f}\033[0m")
    print(f"Monte Carlo area N \033[92m{n}\033[0m  integrate f(x) from {a} to {b}: \033[92m{monte_carlo_integration_area(a, b, 1.6, f, n):.6f}\033[0m")
    n=5000000
    print(f"Monte Carlo mean N \033[92m{n}\033[0m integrate f(x) from {a} to {b}: \033[92m{monte_carlo_integration_mean(a, b, f, n):.6f}\033[0m")
    print(f"Monte Carlo area N \033[92m{n}\033[0m integrate f(x) from {a} to {b}: \033[92m{monte_carlo_integration_area(a, b, 1.6, f, n):.6f}\033[0m")
