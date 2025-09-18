"""
Lista 10 - Cálculo de Autovalores e Autovetores
Yhasmim de Souza Tigre - 20210026966
"""
import numpy as np
import lista10_fun_aux_20210026966 as aux

def main():
    print("=== Cálculo de Autovalores e Autovetores ===")
    try:
        m = int(input("Digite o tamanho da matriz quadrada m (ex: 2): "))
        print(f"Digite as {m} linhas da matriz A, separando os elementos por espaço:")

        A = []
        for i in range(m):
            linha = list(map(float, input(f"Linha {i+1}: ").split()))
            if len(linha) != m:
                raise ValueError("Número de elementos inválido na linha.")
            A.append(linha)

        A = np.array(A)
        print("\nMatriz A:")
        print(A)

        autovalores, autovetores = aux.autovalores_autovetores(A)
        
        while True:
            resposta = input("Deseja fazer interações com autovetores? (s/n): ").strip().lower()
            if resposta == 's': 
                aux.calculo_extra_vetores(A, autovalores, autovetores, m)
            if resposta == 'n':
                break
            else:
                print("Por favor, digite 's' para sim ou 'n' para não.")

        if m in [2, 3]:
            aux.plotar_autovetores(autovalores, autovetores)
            print(f"Imagens salvas como 'matriz {m}x{m}.png'")
        else:
            print("\nPlotagem disponível apenas para matrizes 2x2 ou 3x3.")
        
    except Exception as e:
        print("Erro:", e)

main()