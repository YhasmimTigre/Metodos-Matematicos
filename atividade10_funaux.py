import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D

def autovalores_autovetores(A):
    # Cálculo de autovalores e autovetores
    autovalores, autovetores = eig(A)
    
    # Arredonda autovalores para facilitar contagem (evitar ruído numérico)
    autovalores_arred = np.round(autovalores, decimals=6)
    
    # Contar multiplicidade dos autovalores
    multiplicidades = Counter(autovalores_arred)

    print("Autovalores e multiplicidades:")
    for val, mult in multiplicidades.items():
        print(f"  λ = {val:.6f}  multiplicidade = {mult}")

    print("\nAutovetores unitários:")
    for i, val in enumerate(autovalores_arred):
        v_unitario = autovetores[:, i] / np.linalg.norm(autovetores[:, i])
        print(f"  λ = {val:.6f}  →  autovetor unitário: {v_unitario}")

    return autovalores_arred, autovetores

def plotar_autovetores(autovalores, autovetores):
    m = autovetores.shape[0]
    autovalores_unicos = np.unique(autovalores)
    cores = plt.cm.get_cmap('tab10', len(autovalores_unicos))

    if m == 2:
        plt.figure()
        for i, val in enumerate(autovalores):
            v = autovetores[:, i]
            v_unit = v / np.linalg.norm(v)
            cor = cores(np.where(autovalores_unicos == val)[0][0])
            plt.quiver(0, 0, v_unit[0], v_unit[1], angles='xy', scale_units='xy', scale=1, color=cor, label=f'λ={val:.2f}')
        plt.axhline(0, color='gray', linewidth=0.5)
        plt.axvline(0, color='gray', linewidth=0.5)
        plt.xlim(-1.5, 1.5)
        plt.ylim(-1.5, 1.5)
        plt.gca().set_aspect('equal')
        plt.legend()
        plt.title("Autovetores unitários (2D)")
        plt.savefig(f'matriz {m}x{m}.png')
        plt.grid(True)
        plt.show()

    elif m == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i, val in enumerate(autovalores):
            v = autovetores[:, i]
            v_unit = v / np.linalg.norm(v)
            cor = cores(np.where(autovalores_unicos == val)[0][0])
            ax.quiver(0, 0, 0, v_unit[0], v_unit[1], v_unit[2], color=cor, label=f'λ={val:.2f}')
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        ax.set_title("Autovetores unitários (3D)")
        plt.savefig(f'matriz {m}x{m}.png')
        ax.legend()
        plt.show()
        

def calculo_extra_vetores(A, autovalores, autovetores, m):
    autovalores_unicos = np.unique(autovalores)
    cores = plt.cm.get_cmap('tab10', len(autovalores_unicos))

    while True:
        try:
            idx = int(input(f"\nEscolha o índice do autovetor (0 a {m-1}, ou -1 para sair): "))
            if idx == -1:
                break
            if idx < 0 or idx >= m:
                print("Índice inválido.")
                continue

            vaut = autovetores[:, idx]
            vaut_unit = vaut / np.linalg.norm(vaut)
            val_autovalor = autovalores[idx]
            cor = cores(np.where(autovalores_unicos == val_autovalor)[0][0])

            entrada = input(f"Digite as {m} coordenadas de um vetor na direção de vaut (ex: 2 4 6): ")
            vdiraut = np.array(list(map(float, entrada.split())))
            if vdiraut.shape[0] != m:
                print(f"Vetor deve ter {m} componentes.")
                continue

            Av = A @ vdiraut
            print(f"A @ vdiraut = {Av}")

            if m == 2:
                plt.figure()
                plt.plot([0, vaut_unit[0]], [0, vaut_unit[1]], color=cor, label="vaut (unitário)")
                plt.plot([0, Av[0]], [0, Av[1]], color=cor, linestyle='--', label="Avdiraut")
                plt.axhline(0, color='gray', linewidth=0.5)
                plt.axvline(0, color='gray', linewidth=0.5)
                plt.xlim(-2, 2)
                plt.ylim(-2, 2)
                plt.gca().set_aspect('equal')
                plt.legend()
                plt.grid(True)
                plt.title("Autovetor e Imagem de vdiraut")
                plt.savefig(f'matriz {m}x{m} + vdiraut.png')
                plt.show()

            elif m == 3:
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.plot([0, vaut_unit[0]], [0, vaut_unit[1]], [0, vaut_unit[2]], color=cor, label="vaut (unitário)")
                ax.plot([0, Av[0]], [0, Av[1]], [0, Av[2]], color=cor, linestyle='--', label="Avdiraut")
                ax.set_xlim([-2, 2])
                ax.set_ylim([-2, 2])
                ax.set_zlim([-2, 2])
                ax.set_title("Autovetor e Imagem de vdiraut")
                plt.savefig(f'matriz {m}x{m} + vdiraut.png')
                ax.legend()
                plt.show()

            else:
                print("Plotagem de vetores para m = 2 ou m = 3.")

        except Exception as e:
            print("Erro:", e)
