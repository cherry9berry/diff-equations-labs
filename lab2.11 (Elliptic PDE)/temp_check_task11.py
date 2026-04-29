"""
Проверка решения задачи №11 (кольцо)
"""
import numpy as np

print("="*60)
print("PROVERKA ZADACHI #11 (KOLTSO)")
print("="*60)

# Параметры
alpha = np.pi / 3

# Коэффициенты
E = 3
G = 1 / np.log(3)
A1 = 1 / 364
B1 = -729 / 364
A2 = 729 / (729**2 - 1)
B2 = -A2

# Аналитическое решение
def u_analytical(r, theta):
    term0 = E + G * np.log(r)
    term1 = (A1 * r**3 + B1 * r**(-3)) * np.cos(3*theta)
    term2 = (A2 * r**6 + B2 * r**(-6)) * np.cos(6*theta)
    return term0 + term1 + term2

# Проверка граничных условий
print("\nProverka granichnyh usloviy:")
theta_test = np.linspace(0, alpha, 100)

# u(1,theta) = 3 - 2*cos(3*theta)
u_at_r1 = u_analytical(1, theta_test)
expected_r1 = 3 - 2 * np.cos(3*theta_test)
error_r1 = np.max(np.abs(u_at_r1 - expected_r1))
print(f"u(1,theta) = 3 - 2*cos(3*theta): max error = {error_r1:.2e}")

# u(3,theta) = 4 + cos(6*theta)
u_at_r3 = u_analytical(3, theta_test)
expected_r3 = 4 + np.cos(6*theta_test)
error_r3 = np.max(np.abs(u_at_r3 - expected_r3))
print(f"u(3,theta) = 4 + cos(6*theta): max error = {error_r3:.2e}")

# Проверка уравнения Лапласа
print("\nProverka uravneniya Laplasa (chislenno):")
r_check = np.linspace(1.1, 2.9, 10)
theta_check = np.linspace(0.01, alpha-0.01, 20)
R_check, THETA_check = np.meshgrid(r_check, theta_check)

h_r = 0.01
h_theta = 0.01
laplacian_error = []

for r, theta in zip(R_check.flat, THETA_check.flat):
    # u_rr
    u_rr = (u_analytical(r+h_r, theta) - 2*u_analytical(r, theta) + u_analytical(r-h_r, theta)) / h_r**2
    # u_r
    u_r = (u_analytical(r+h_r, theta) - u_analytical(r-h_r, theta)) / (2*h_r)
    # u_theta_theta
    u_tt = (u_analytical(r, theta+h_theta) - 2*u_analytical(r, theta) + u_analytical(r, theta-h_theta)) / h_theta**2
    
    # Лапласиан в полярных координатах
    laplacian = u_rr + (1/r)*u_r + (1/r**2)*u_tt
    laplacian_error.append(np.abs(laplacian))

max_laplacian_error = np.max(laplacian_error)
print(f"Delta u = 0: max error = {max_laplacian_error:.2e}")

print("\n" + "="*60)
if error_r1 < 1e-10 and error_r3 < 1e-10 and max_laplacian_error < 0.1:
    print("RESHENIE PRAVILNOE!")
else:
    print("VNIMANIE: Est oshibki")
print("="*60)

