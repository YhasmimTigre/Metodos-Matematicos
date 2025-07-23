import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def entradas():
    """Obtém as entradas do usuário e valida as restrições."""
    f_expr = input("Digite a expressão da função f(x): ")
    a = float(input("Digite o centro a: "))
    
    Kmin = int(input("Digite Kmin: "))
    Kmax = int(input("Digite Kmax (deve ser >= Kmin + 3): "))
    while Kmax < Kmin + 3:
        print("Kmax deve ser pelo menos Kmin + 3")
        Kmax = int(input("Digite Kmax novamente: "))
    
    xmin = float(input("Digite xmin (xmin < a): "))
    while xmin >= a:
        print("xmin deve ser menor que a")
        xmin = float(input("Digite xmin novamente: "))
    
    xmax = float(input("Digite xmax (xmax > a): "))
    while xmax <= a:
        print("xmax deve ser maior que a")
        xmax = float(input("Digite xmax novamente: "))
    
    R_input = input("Digite o raio de convergência R (ou 'inf' para infinito): ")
    R = float('inf') if R_input.lower() == 'inf' else float(R_input)
    
    delta = 0.0
    if R != float('inf'):
        delta = float(input("Digite o valor de δ > 0: "))
        while delta <= 0:
            delta = float(input("δ deve ser > 0. Digite novamente: "))
    
    return f_expr, a, Kmin, Kmax, xmin, xmax, R, delta

def calcular_polinomios_taylor(f_expr, a, Kmin, Kmax):
    """Calcula os polinômios de Taylor de ordem Kmin até Kmax."""
    x = sp.symbols('x')
    f = sp.sympify(f_expr)
    polinomios = {}
    
    for k in range(Kmin, Kmax + 1):
        taylor = 0
        for n in range(k + 1):
            derivada = f.diff(x, n)
            derivada_em_a = derivada.subs(x, a)
            termo = (derivada_em_a / sp.factorial(n)) * (x - a)**n
            taylor += termo
        polinomios[k] = sp.lambdify(x, taylor, 'numpy')
    
    f_lamb = sp.lambdify(x, f, 'numpy')
    return polinomios, f_lamb

def preparar_intervalos_plotagem(xmin, xmax, a, R, delta):
    """Prepara os intervalos de plotagem considerando o raio de convergência."""
    x_vals = np.linspace(xmin, xmax, 1000)
    intervalos_seguros = []
    intervalos_inseguros = []
    
    if R == float('inf'):
        intervalos_seguros.append(x_vals)
    else:
        # Intervalo seguro
        seg_min = max(xmin, a - R + delta)
        seg_max = min(xmax, a + R - delta)
        if seg_min < seg_max:
            intervalos_seguros.append(np.linspace(seg_min, seg_max, 500))
        
        # Intervalos inseguros
        if xmin < a - R + delta:
            intervalos_inseguros.append(np.linspace(xmin, a - R + delta, 100))
        if xmax > a + R - delta:
            intervalos_inseguros.append(np.linspace(a + R - delta, xmax, 100))
    
    return x_vals, intervalos_seguros, intervalos_inseguros

def plotar_graficos(f_lamb, polinomios, a, Kmin, Kmax, xmin, xmax, 
                   intervalos_seguros, intervalos_inseguros, f_expr):
    """Plota os gráficos da função e dos polinômios de Taylor."""
    plt.figure(figsize=(12, 8))
    
    # Plotar função nos intervalos seguros
    for intervalo in intervalos_seguros:
        plt.plot(intervalo, f_lamb(intervalo), 'k-', linewidth=2, label=f'f(x) = {f_expr}')
    
    # Plotar função nos intervalos inseguros
    for intervalo in intervalos_inseguros:
        plt.plot(intervalo, f_lamb(intervalo), 'k--', linewidth=1, alpha=0.4)
    
    # Plotar polinômios de Taylor
    colors = plt.cm.viridis(np.linspace(0, 1, Kmax - Kmin + 1))
    for i, k in enumerate(range(Kmin, Kmax + 1)):
        y_vals = polinomios[k](np.linspace(xmin, xmax, 1000))
        plt.plot(np.linspace(xmin, xmax, 1000), y_vals, '--', color=colors[i], 
                 linewidth=1.5, label=f'P_{k}(x)')
    
    # Configurações do gráfico
    plt.axvline(a, color='gray', linestyle='--', alpha=0.5)
    plt.title(f'Polinômios de Taylor de f(x) em x = {a}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='best', fontsize=8)
    plt.xlim(xmin, xmax)
    plt.tight_layout()
    plt.savefig('taylor_series.png', dpi=300)
    plt.show()