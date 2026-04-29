# Lab 1.5: Fourier Series Expansion

## Overview
This laboratory work investigates the representation of periodic functions as an infinite sum of simple sine and cosine waves, known as the **Fourier Series**.

## Physical Interpretation
The Fourier series is based on the principle of **superposition**. Almost any complex periodic signal (like a musical note or a square wave in a circuit) can be decomposed into a sum of fundamental and harmonic frequencies. In this lab, we approximate a square wave by adding its harmonics.

## Mathematical Model
A periodic function $f(x)$ with period $2\pi$ can be expanded as:
$$f(x) \approx \sum_{n=1,3,5,...}^{N} \frac{4}{\pi n} \sin(nx)$$

This specifically describes the **square wave** used in the lab. Key observations include:
- **Convergence:** As the number of terms $N$ increases, the sum closer approximates the square wave.
- **Gibbs Phenomenon:** Near the jump discontinuities, there is a characteristic "ringing" or overshoot that does not disappear even as $N \to \infty$.

## Implementation details
The lab visualizes the partial sums for $N = [1, 3, 10, 50]$. It demonstrates how higher frequencies "sharpen" the edges of the wave and how the energy of the signal is distributed across its spectrum.
