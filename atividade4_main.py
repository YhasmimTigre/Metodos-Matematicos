import numpy as np
import matplotlib.pyplot as plt

def encontrar_pares(L: float, Q: int, epsilon: float):
    """
    Encontra os Q primeiros índices nk tais que |cos(nk) - L| < epsilon.
    
    Retorna duas listas: [nk], [ank]
    """
    nk_list = []
    ank_list = []
    n = 0

    while len(nk_list) < Q:
        a_n = np.cos(n)
        if abs(a_n - L) < epsilon:
            nk_list.append(n)
            ank_list.append(a_n)
        n += 1

    return nk_list, ank_list


def plotar_pares(nk_list, ank_list, L, epsilon):
    """
    Plota os pares (nk, ank) com linhas de referência em L ± epsilon.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(nk_list, ank_list, 'bo-', label='ank = cos(nk)')
    plt.axhline(L, color='red', linestyle='--', label=f'L = {L}')
    plt.axhline(L + epsilon, color='gray', linestyle=':', label=f'L ± ε')
    plt.axhline(L - epsilon, color='gray', linestyle=':')
    plt.xlabel('nk')
    plt.ylabel('ank = cos(nk)')
    plt.title(f'{len(nk_list)} pares (nk, ank) com |cos(nk) - L| < ε')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    # Parâmetros de entrada
    L = 0.5          # valor alvo entre -1 e 1
    Q = 10           # número de pares desejados
    epsilon = 0.01   # tolerância

    # Cálculo dos pares
    nk_list, ank_list = encontrar_pares(L, Q, epsilon)

    # Impressão dos pares
    print("Pares (nk, ank):")
    for nk, ank in zip(nk_list, ank_list):
        print(f"({nk}, {ank:.6f})")

    # Plotagem
    plotar_pares(nk_list, ank_list, L, epsilon)


main()
