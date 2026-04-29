"""
Проверка решения задачи №9 (внутренняя задача)
"""
import numpy as np

print("="*60)
print("PROVERKA ZADACHI #9 (VNUTRENNYAYA)")
print("="*60)

# Аналитическое решение
def u_analytical(r, theta):
    return -r**3 * np.cos(3*theta) - r**4 * np.sin(4*theta)

# Проверка граничного условия
print("\nProverka granichnogo usloviya u(1,theta):")
theta_test = np.linspace(0, 2*np.pi, 100)
u_at_r1 = u_analytical(1, theta_test)
expected = -np.cos(3*theta_test) - np.sin(4*theta_test)
error = np.max(np.abs(u_at_r1 - expected))
print(f"u(1,theta) = -cos(3*theta) - sin(4*theta): max error = {error:.2e}")

# Проверка уравнения Лапласа в полярных координатах
print("\nProverka uravneniya Laplasa (chislenno):")
r_check = np.linspace(0.1, 0.9, 10)
theta_check = np.linspace(0.1, 2*np.pi-0.1, 20)
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
    
    # Лапласиан в полярных координатах: u_rr + (1/r)*u_r + (1/r^2)*u_theta_theta
    laplacian = u_rr + (1/r)*u_r + (1/r**2)*u_tt
    laplacian_error.append(np.abs(laplacian))

max_laplacian_error = np.max(laplacian_error)
print(f"Delta u = 0: max error = {max_laplacian_error:.2e}")

print("\n" + "="*60)
if error < 1e-10 and max_laplacian_error < 0.1:
    print("RESHENIE PRAVILNOE!")
else:
    print("VNIMANIE: Est oshibki")
print("="*60)

