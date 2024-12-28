def obter_coluna(numero):
    """Retorna a coluna (1, 2 ou 3) de um número sorteado."""
    if numero in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
        return 1
    elif numero in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
        return 2
    elif numero in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
        return 3
    return None


def obter_duzia(numero):
    """Retorna a dúzia (1, 2 ou 3) de um número sorteado."""
    if 1 <= numero <= 12:
        return 1
    elif 13 <= numero <= 24:
        return 2
    elif 25 <= numero <= 36:
        return 3
    return None


def sugerir_apostas(numeros):
    """Gera sugestões de apostas com base nos últimos números sorteados."""
    if len(numeros) < 2:
        return "Insira pelo menos 2 números para gerar uma recomendação."
    
    coluna_ultimos = [obter_coluna(num) for num in numeros[-2:]]
    duzia_ultimos = [obter_duzia(num) for num in numeros[-2:]]
    
    recomendacao = []

    if coluna_ultimos[0] == coluna_ultimos[1]:
        colunas_possiveis = [1, 2, 3]
        colunas_possiveis.remove(coluna_ultimos[0])
        recomendacao.append(f"Os últimos 2 números estão na mesma coluna ({coluna_ultimos[0]}). Aposte nas colunas {colunas_possiveis}.")
    else:
        recomendacao.append("Os últimos 2 números não estão na mesma coluna.")

    if duzia_ultimos[0] == duzia_ultimos[1]:
        duzias_possiveis = [1, 2, 3]
        duzias_possiveis.remove(duzia_ultimos[0])
        recomendacao.append(f"Os últimos 2 números estão na mesma dúzia ({duzia_ultimos[0]}). Aposte nas dúzias {duzias_possiveis}.")
    else:
        recomendacao.append("Os últimos 2 números não estão na mesma dúzia.")

    return " ".join(recomendacao)


# Início do programa
numeros_sorteados = []

while True:
    print(f"Últimos números sorteados: {numeros_sorteados}")
    entrada = input("Digite o próximo número sorteado (ou 'sair' para encerrar): ")

    if entrada.lower() == 'sair':
        print("Encerrando o programa.")
        break

    try:
        numero = int(entrada)
        
        if numero < 0 or numero > 36:
            print("Por favor, insira um número entre 0 e 36.")
            continue

        numeros_sorteados.append(numero)
        if len(numeros_sorteados) > 10:
            numeros_sorteados.pop(0)

        print(sugerir_apostas(numeros_sorteados))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido ou 'sair' para encerrar.")
