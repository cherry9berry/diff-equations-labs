# Lab 1.6: Mathematical Modeling (Newton's Law of Cooling)

## Overview
This laboratory work applies the principles of differential equations to a real-world physical process: the cooling of an object in a surrounding medium, governed by **Newton's Law of Cooling**.

## Physical Interpretation
Newton's law states that the rate of change of the temperature of an object is proportional to the difference between its own temperature and the ambient (environmental) temperature. 
- A hot cup of coffee cools faster when first poured than when it is close to room temperature.
- The constant $k$ represents the thermal properties of the object and the efficiency of heat transfer.

## Mathematical Model
The process is modeled by the first-order linear ODE:
$$\frac{dT}{dt} = -k(T - T_{env})$$

Where:
- $T(t)$ is the temperature at time $t$.
- $T_{env}$ is the constant temperature of the environment.
- $k > 0$ is the cooling constant.

The solution is an exponential decay towards the ambient temperature:
$$T(t) = T_{env} + (T_0 - T_{env})e^{-kt}$$

## Implementation details
The lab simulates the cooling process for different values of $k$ ($0.05, 0.1, 0.2$) starting from index $T_0 = 100^\circ C$ in an environment of $22^\circ C$. It uses numerical integration (Euler method) to visualize how quickly the system reaches equilibrium.
