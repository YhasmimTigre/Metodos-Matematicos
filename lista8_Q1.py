import numpy as np
import matplotlib.pyplot as plt

# Definição das derivadas necessárias
def f2(x):  # Segunda derivada = cosh(x)
    return np.cosh(x)

def f3(x):  # Terceira derivada = sinh(x)
    return np.sinh(x)

# Intervalo de análise
x_vals = np.linspace(0, 0.1, 1000)

# Avaliação das derivadas no intervalo
f2_vals = np.abs(f2(x_vals))
f3_vals = np.abs(f3(x_vals))

# Estimar os máximos (M)
M_linear = np.max(f2_vals)      # Para erro da aproximação linear
M_quadratica = np.max(f3_vals)  # Para erro da aproximação quadrática

# Cálculo dos erros com x = 0.1
x = 0.1
R1 = M_linear * (x**2) / 2
R2 = M_quadratica * (x**3) / 6

# Resultados
print(f"Máximo da segunda derivada no intervalo [0, 0.1]: {M_linear:.10f}")
print(f"Máximo da terceira derivada no intervalo [0, 0.1]: {M_quadratica:.10f}")
print(f"Erro da aproximação linear em x=0.1: {R1:.10e}")
print(f"Erro da aproximação quadrática em x=0.1: {R2:.10e}")

# Gráficos (opcional)
plt.plot(x_vals, f2_vals, label='|f\'\'(x)| = |cosh(x)|')
plt.plot(x_vals, f3_vals, label='|f\'\'\'(x)| = |sinh(x)|')
plt.title("Derivadas absolutas no intervalo [0, 0.1]")
plt.legend()
plt.grid(True)
plt.show()
