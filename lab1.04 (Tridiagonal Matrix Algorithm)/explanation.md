# Lab 1.4: Tridiagonal Matrix Algorithm (Thomas Algorithm)

## Overview
This laboratory work explores the **Tridiagonal Matrix Algorithm (TDMA)**, also known as the **Thomas Algorithm**, to solve Boundary Value Problems (BVP) for second-order differential equations.

## Physical Interpretation
While the previous labs solved evolution problems (time-dependent), this lab solves a stationary distribution problem. A classic example is the **temperature distribution in a rod** where the values at the ends are fixed (Dirichlet boundary conditions). The internal temperature stabilizes according to the heat sources within the rod.

## Mathematical Model
Given the BVP:
$$y'' = f(x), \quad y(0) = a, \quad y(L) = b$$

Using central finite differences, we discretize the second derivative:
$$\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} = f_i$$

This leads to a system of linear equations $Ay = B$, where $A$ is a **tridiagonal matrix**:
$$a_i y_{i-1} + b_i y_i + c_i y_{i+1} = d_i$$

TDMA solves this system in two passes:
1. **Forward pass:** Calculate recursive coefficients $\alpha$ and $\beta$.
2. **Backward pass:** Determine the values of $y_i$ starting from the end boundary.

## Implementation details
The lab implements the algorithm for a rod discretized into $N$ points. It demonstrates that TDMA is highly efficient, with $O(N)$ computational complexity compared to $O(N^3)$ for generic Gaussian elimination.
