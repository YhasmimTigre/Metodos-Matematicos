""" Atividade 1 - métodos matemáticos
    Yhasmim de Souza Tigre - 20210026966
"""
import numpy as np
import matplotlib.pyplot as plt
import os

def ler_sequencias():
    print("Escolha uma das sequências da lista:")

    sequencias = {
        "d": "(4*n**2 - 3*n) / (n**2 + 5*n - 6)",
        "j": "(3**n + 4**n)**(1/n)",
        "f": "(1 + 1/(3*n))**n",
        "b": "1/(3**n) + (3/4)**(n - 3)",
        "h": "n / (np.e**n)"
    }

    for k, v in sequencias.items():
        print(f"Item {k}) a(n) = {v}")

    escolha = input("Digite a letra da sequência desejada (ex: d): ").lower()
    while escolha not in sequencias:
        escolha = input("Entrada inválida. Digite novamente (ex: d, j, f, b ou h): ").lower()

    try:
        nmin = int(input("Digite o valor de nmin: "))
        nmax = int(input("Digite o valor de nmax: "))
        while nmin >= nmax:
            print("nmin deve ser menor que nmax.")
            nmin = int(input("Digite o valor de nmin: "))
            nmax = int(input("Digite o valor de nmax: "))
    except ValueError:
        print("Entrada inválida. Os valores devem ser inteiros.")
        return None, None, None, None, None, None, None

    print("\nVocê sabe se a sequência é convergente para um limite?")
    print("\n1 - Não sei se é convergente")
    print("\n2 - Sei que converge para um limite L")
    opcao = input("\nEscolha 1 ou 2: ").strip()

    if opcao == "2":
        try:
            L = float(input("Digite o valor do limite L: "))
            epsilon = float(input("Digite o valor da tolerância ε: "))
            N_epsilon = int(input("Digite o valor de N(ε): "))
        except ValueError:
            print("Entradas inválidas.")
            return None, None, None, None, None, None, None
        return sequencias[escolha], nmin, nmax, L, epsilon, N_epsilon, escolha

    return sequencias[escolha], nmin, nmax, None, None, None, escolha

def termo_geral(expr, nmin, nmax):
    #dicionário para entender expressões matemáticas
    allowed_names = {
        "np": np,
        "sqrt": np.sqrt,
        "log": np.log,
        "ln": np.log,
        "exp": np.exp,
        "e": np.e,
        "pi": np.pi,
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "n": None  # será atribuído a cada iteração
    }

    def a(n):
        local_env = allowed_names.copy()
        local_env["n"] = n
        return eval(expr, {"__builtins__": {}}, local_env)

    # Gera os valores de n e os correspondentes a(n)
    n_vals = np.arange(nmin, nmax + 1)
    a_vals = np.array([a(n) for n in n_vals])

    return n_vals, a_vals


def verificar_convergencia(n_vals, a_vals, L, epsilon, N_epsilon):
    #Aqui verifica-se se a sequência converger para os valores recebidos (true or false)
    if L is None or epsilon is None or N_epsilon is None:
        print("O usuário escolheu a opção 1, logo não temos parâmetros de convergência para serem verificados.")
        return False

    verificado = True
    for n, a in zip(n_vals, a_vals):
        if n >= N_epsilon:
            erro = abs(a - L)
            if erro > epsilon:
                print(f"❌ Violação: |a({n}) - {L}| = {erro:.6f} > ε = {epsilon}")
                verificado = False

    if verificado:
        print("✅ Todos os valores de a(n) com n ≥ N(ε) satisfazem |a(n) - L| ≤ ε.")
    else:
        print("⚠️ Nem todos os termos a(n) após N(ε) estão dentro da tolerância.")
    
    return verificado

    
def tabela(n_vals, a_vals, nome_arquivo):
    # Mostrar os resultados do termo geral e cria um arquivo txt
    print("Tabela de pares (n, a(n))")

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write("Tabela de pares (n, a(n))\n")
        for n, a in zip(n_vals, a_vals):
            linha = f"n = {n}, a(n) = {a:.6f}"
            print(linha)
            f.write(linha + '\n')

    print(f"\n✅ Tabela exportada para o arquivo '{nome_arquivo}' com sucesso.")

def grafico(item_questao, n_vals, a_vals, L=None, epsilon=None, N_epsilon=None):
        titulo = f"Gráfico da sequência a(n) do item '{item_questao}'"
        plt.figure(figsize=(10, 5))
        plt.plot(n_vals, a_vals, 'bo-', label='a(n)')

        pasta = "figuras_plot_20210026966"
        nome_arquivo = f"{pasta}/grafico_item_{item_questao}.png"

        verificado = verificar_convergencia(n_vals, a_vals, L, epsilon, N_epsilon)

        if verificado:
            plt.axhline(L, color='red', linestyle='--', linewidth=1.5, label='L')
            plt.axhline(L + epsilon, color='green', linestyle='--', linewidth=1.0, label='L + ε')
            plt.axhline(L - epsilon, color='green', linestyle='--', linewidth=1.0, label='L - ε')
            plt.axvline(x = N_epsilon, color='blue', linestyle='--', linewidth=1.0, label='N(ε)')
            titulo += " (convergência verificada)"
            nome_arquivo = f"{pasta}/grafico_item_{item_questao}_com_L.png"
        
        plt.xlabel("n (índice)")
        plt.ylabel("a(n) (valor da sequência)")
        plt.title(titulo)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        if not os.path.exists(pasta):
            os.makedirs(pasta)
        
        plt.savefig(nome_arquivo)
        print(f"✅ Gráfico salvo em: {nome_arquivo}")

        plt.show()