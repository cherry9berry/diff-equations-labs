# Lab 1.3: Adams Multi-step Methods

## Overview
This laboratory work focuses on the **Adams-Bashforth method**, which belongs to the class of multi-step methods. Unlike Runge-Kutta, multi-step methods use values from several previous steps to predict the future state.

## Physical Interpretation
Multi-step methods have "memory". Instead of throwing away previous calculations, they use the trend from earlier positions to extrapolate the next point. In terms of physics, this is like considering the inertia or history of movement to find the next coordinate.

## Mathematical Model
The **2-step Adams-Bashforth method** is defined as:
$$y_{n+1} = y_n + \frac{h}{2} [3f(x_n, y_n) - f(x_{n-1}, y_{n-1})]$$

Because the method requires previous history (e.g., $y_{n-1}$), it cannot start on its own. A one-step method like **RK4** is typically used to generate the first few required points.

## Implementation details
This lab implements the 2-step method for $y' = y - x^2 + 1$. The numerical solution demonstrates competitive accuracy with RK4 while potentially requiring fewer function evaluations per step once the history is established.
