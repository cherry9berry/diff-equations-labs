# Lab 1.1: Euler Methods for ODEs

## Overview
This laboratory work explores the most fundamental numerical methods for solving Initial Value Problems (IVP) for first-order Ordinary Differential Equations (ODEs). The focus is on the **Simple Euler Method** (explicit) and the **Modified Euler Method** (Heun's method).

## Physical Interpretation
Numerical integration of an ODE can be thought of as finding the trajectory of a point moving in a velocity field. 
- The **Simple Euler method** assumes the velocity remains constant over a small time step $h$.
- The **Modified Euler method** samples the velocity at the beginning and the predicted end of the step, averaging them for better accuracy.

## Mathematical Model
Given the IVP:
$$\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0$$

### 1. Simple Euler Method (Explicit)
Calculates the next point by following the tangent line at the current point:
$$y_{n+1} = y_n + h \cdot f(x_n, y_n)$$

### 2. Modified Euler Method (Heun)
Uses a predictor-corrector approach to improve the estimate:
$$\text{Predictor: } \tilde{y}_{n+1} = y_n + h \cdot f(x_n, y_n)$$
$$\text{Corrector: } y_{n+1} = y_n + \frac{h}{2} [f(x_n, y_n) + f(x_{n+1}, \tilde{y}_{n+1})]$$

## Implementation details
In this lab, the equation $y' = y - x^2 + 1$ is solved. The error analysis compares numerical results with the analytical solution to demonstrate the $O(h)$ and $O(h^2)$ convergence rates.
