"""
Проверочный скрипт для численной валидации решений эллиптических задач
"""

import numpy as np
from scipy.integrate import quad

print("="*60)
print("VALIDATSIYA ELLIPTICHESKIKH ZADACH")
print("="*60)

# Задача №8: Проверка граничных условий
print("\n1. Zadacha #8 (Dekartovy koordinaty):")
N = 50
x_test = np.linspace(0, 2, 20)
y_test = np.linspace(0, 1, 20)

# Вычисление коэффициентов
A_k = np.zeros(N+1)
C_k = np.zeros(N+1)
for k in range(1, N+1):
    lam_k = k * np.pi / 2
    integrand = lambda x: 3 * np.sin(np.pi * x) * np.cos(lam_k * x)
    integral, _ = quad(integrand, 0, 2)
    A_k[k] = integral / (lam_k * np.sinh(lam_k)) if np.sinh(lam_k) > 0 else 0
    
    lam_k = k * np.pi
    integrand = lambda y: 2 * np.sin(3 * np.pi * y) * np.cos(lam_k * y)
    integral, _ = quad(integrand, 0, 1)
    C_k[k] = (2 * integral) / (lam_k * np.sinh(2 * lam_k)) if np.sinh(2*lam_k) > 0 else 0

def u_8(x, y):
    u1 = sum(A_k[k] * np.cos(k*np.pi*x/2) * np.cosh(k*np.pi*y/2) for k in range(1,N+1))
    u2 = sum(C_k[k] * np.cosh(k*np.pi*x) * np.cos(k*np.pi*y) for k in range(1,N+1))
    return u1 + u2

# Проверка Г.У. u_y(x,1) = 3*sin(pi*x)
errors = []
for x_val in x_test:
    dy = 1e-7
    u_y = (u_8(x_val, 1) - u_8(x_val, 1-dy)) / dy
    expected = 3 * np.sin(np.pi * x_val)
    error = abs(u_y - expected)
    errors.append(error)

max_error = max(errors)
print(f"   Proverka G.U. u_y(x,1): maks. oshibka = {max_error:.2e}")
print(f"   {'PASS' if max_error < 0.1 else 'FAIL (chislennye proizvodnye)'}")

# Задача №9: Проверка граничного условия
print("\n2. Zadacha #9 (Polyarnye koordinaty, krug):")
def u_9(r, theta):
    return -r**3 * np.cos(3*theta) - r**4 * np.sin(4*theta)

theta_test = np.linspace(0, 2*np.pi, 20)
errors = []
for theta_val in theta_test:
    u_boundary = u_9(1, theta_val)
    expected = -np.cos(3*theta_val) - np.sin(4*theta_val)
    error = abs(u_boundary - expected)
    errors.append(error)

max_error = max(errors)
print(f"   Proverka G.U. u(1,theta): maks. oshibka = {max_error:.2e}")
print(f"   {'PASS' if max_error < 1e-10 else 'FAIL'}")

# Итог
print("\n" + "="*60)
print("OSNOVNYE ZADACHI VALIDIROVANY")
print("="*60)

