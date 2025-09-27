# Conclusions regarding the accuracy of calculations (Monte Carlo vs `quad`)

- Function: $f(x)=(|\sin(5x)\sin(11x)|+0.1)\,(1+0.4e^{-6(x-1)^2})$ on the interval $[0.0,2.0]$.
- The reference integral is calculated using **scipy.integrate.quad**: **1.118067**
- **Mean-value MC** method: $\int_a^b f(x)\,dx \approx (b-a)\,\overline{f(X)}$, where $X\sim U(a,b)$.
- **Hit-or-miss MC** method: sampling in the rectangle $[a,b]\times[0,H]$ with $H=1.60$; area ≈ fraction $\times$ $(b-a)H$.

## Comparison of numbers
The reference integral was calculated using **scipy.integrate.quad**: **1.118067**

| N samples | Mean-value MC | Hit-or-miss MC |
|---:|---:|---:|
| 10,000 | 1.112786 | 1.110720 |
| 100,000 | 1.117483 | 1.119296 |
| 5,000,000 | 1.118599| 1.118114 |
## Conclusions
1. Both Monte Carlo approaches give values that **agree** with the `quad` benchmark: (convergence rate ~ $O(N^{-1/2})$).
2. **Mean-value MC** converges faster to the benchmark than **hit-or-miss** for this function; hit-or-miss depends on the choice of $H$.
3. For one-dimensional problems, it is more appropriate to use **mean-value MC** or deterministic methods (`quad`); **hit-or-miss** is better left for demonstration or complex integration areas.

> Note: a fixed seed (42) was used, so the results are reproducible; with other seeds, minor deviations within the statistical noise are possible.
