import atividade7_funaux_20210026966_yhasmim as aux

def main():
    """Função principal que orquestra o processo."""
    # Obter entradas do usuário
    entradas = aux.entradas()
    f_expr, a, Kmin, Kmax, xmin, xmax, R, delta = entradas
    
    # Calcular polinômios de Taylor
    polinomios, f_lamb = aux.calcular_polinomios_taylor(f_expr, a, Kmin, Kmax)
    
    # Preparar intervalos de plotagem
    x_vals, intervalos_seguros, intervalos_inseguros = aux.preparar_intervalos_plotagem(
        xmin, xmax, a, R, delta
    )
    
    # Plotar gráficos
    aux.plotar_graficos(f_lamb, polinomios, a, Kmin, Kmax, xmin, xmax,
                   intervalos_seguros, intervalos_inseguros, f_expr)

main()