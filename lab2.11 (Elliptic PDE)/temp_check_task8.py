"""
Проверка решения задачи №8
Сравнение аналитического решения с граничными условиями
"""
import numpy as np

print("="*60)
print("PROVERKA ZADACHI #8")
print("="*60)

# Аналитическое решение (ИСПРАВЛЕНО: sinh(3*pi*x) вместо sinh(6*pi*x))
def u_analytical(x, y):
    term1 = (3 / np.sinh(np.pi)) * np.sin(np.pi * x) * np.sinh(np.pi * y)
    term2 = (2 / np.sinh(6 * np.pi)) * np.sinh(3 * np.pi * x) * np.sin(3 * np.pi * y)
    return term1 + term2

# Проверка граничных условий
print("\nProverka granichnyh usloviy:")
y_test = np.linspace(0, 1, 100)
x_test = np.linspace(0, 2, 100)

# u(0,y) = 0
u_at_x0 = u_analytical(0, y_test)
error_x0 = np.max(np.abs(u_at_x0))
print(f"u(0,y) = 0: max error = {error_x0:.2e}")

# u(x,0) = 0
u_at_y0 = u_analytical(x_test, 0)
error_y0 = np.max(np.abs(u_at_y0))
print(f"u(x,0) = 0: max error = {error_y0:.2e}")

# u(2,y) = 2*sin(3*pi*y)
u_at_x2 = u_analytical(2, y_test)
expected_x2 = 2 * np.sin(3 * np.pi * y_test)
error_x2 = np.max(np.abs(u_at_x2 - expected_x2))
print(f"u(2,y) = 2*sin(3*pi*y): max error = {error_x2:.2e}")

# u(x,1) = 3*sin(pi*x)
u_at_y1 = u_analytical(x_test, 1)
expected_y1 = 3 * np.sin(np.pi * x_test)
error_y1 = np.max(np.abs(u_at_y1 - expected_y1))
print(f"u(x,1) = 3*sin(pi*x): max error = {error_y1:.2e}")

# Проверка уравнения Лапласа (численно)
print("\nProverka uravneniya Laplasa (chislenno):")
x_check = np.linspace(0.1, 1.9, 20)
y_check = np.linspace(0.1, 0.9, 20)
X_check, Y_check = np.meshgrid(x_check, y_check)

h = 0.01
laplacian_error = []
for xi, yi in zip(X_check.flat, Y_check.flat):
    u_xx = (u_analytical(xi+h, yi) - 2*u_analytical(xi, yi) + u_analytical(xi-h, yi)) / h**2
    u_yy = (u_analytical(xi, yi+h) - 2*u_analytical(xi, yi) + u_analytical(xi, yi-h)) / h**2
    laplacian = u_xx + u_yy
    laplacian_error.append(np.abs(laplacian))

max_laplacian_error = np.max(laplacian_error)
print(f"Delta u = 0: max error = {max_laplacian_error:.2e}")

print("\n" + "="*60)
if error_x0 < 1e-10 and error_y0 < 1e-10 and error_x2 < 1e-10 and error_y1 < 1e-10 and max_laplacian_error < 0.1:
    print("RESHENIE PRAVILNOE!")
else:
    print("VNIMANIE: Est oshibki")
    if error_x2 > 1e-10:
        print(f"  - Oshibka na granice x=2: {error_x2:.2e}")
print("="*60)
