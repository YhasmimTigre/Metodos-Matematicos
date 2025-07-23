""" Atividade 1 - métodos matemáticos
    Yhasmim de Souza Tigre - 20210026966
"""
import funcoes_aux_20210026966_yhasmim as aux
def main():
    #Inicialmente, a função a seguir ler os valores de input do usuário
    expr, nmin, nmax, L, epsilon, N_epsilon, item_questao = aux.ler_sequencias()

    #A função termo_geral gera os valores a(n) para cada n que pertence a [nmin, nmax] 
    n_vals, a_vals = aux.termo_geral(expr, nmin, nmax)

    #apresenta a tabela 
    aux.tabela(n_vals, a_vals, nome_arquivo= f'tabela_item_{item_questao}.txt')

    #apresenta o gráfico
    aux.grafico(item_questao, n_vals, a_vals, L, epsilon, N_epsilon)

main()