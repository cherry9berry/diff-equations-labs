# Lab 1.2: Runge-Kutta 4th Order Method (RK4)

## Overview
This laboratory work investigates the classical **4th Order Runge-Kutta method (RK4)**. RK4 is the "workhorse" of numerical ODE solvers, offering a high balance between computational efficiency and accuracy.

## Physical Interpretation
While the Euler method follows a single tangent, RK4 samples the velocity at four distinct points (start, mid-point with two different estimates, and end) to construct a highly accurate prediction of the state at the next time step. This is analogous to surveying the terrain multiple times before deciding on the path.

## Mathematical Model
Given the IVP:
$$\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0$$

The next value $y_{n+1}$ is computed as:
$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

The coefficients are:
- $k_1 = f(x_n, y_n)$
- $k_2 = f(x_n + \frac{h}{2}, y_n + \frac{h \cdot k_1}{2})$
- $k_3 = f(x_n + \frac{h}{2}, y_n + \frac{h \cdot k_2}{2})$
- $k_4 = f(x_n + h, y_n + h \cdot k_3)$

## Implementation details
In this lab, the method is tested against $y' = y - x^2 + 1$. The main objective is to verify that the error decreases as $O(h^4)$, showing the significant improvement over Euler-based methods.
