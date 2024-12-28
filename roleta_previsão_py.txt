def coluna(numero):
    """Determina a coluna de um número da roleta."""
    if numero == 0:
        return 0  # Número zero não pertence a nenhuma coluna
    return (numero - 1) % 3 + 1

def duzia(numero):
    """Determina a dúzia de um número da roleta."""
    if numero == 0:
        return 0  # Número zero não pertence a nenhuma dúzia
    return (numero - 1) // 12 + 1

def recomendar_aposta(ultimos_numeros):
    """Recomenda colunas ou dúzias para apostar com base nos últimos 3 números."""
    if len(ultimos_numeros) < 3:
        return "Insira pelo menos 3 números para gerar uma recomendação."

    # Pega os 3 últimos números
    ultimos_3 = ultimos_numeros[-3:]

    # Verifica se os 3 números pertencem à mesma coluna
    colunas = [coluna(n) for n in ultimos_3]
    if colunas[0] == colunas[1] == colunas[2]:
        col = colunas[0]
        colunas_restantes = [c for c in [1, 2, 3] if c != col]
        return f"Os últimos 3 números estão na mesma coluna ({col}). Aposte nas colunas {colunas_restantes}."

    # Verifica se os 3 números pertencem à mesma dúzia
    duzias = [duzia(n) for n in ultimos_3]
    if duzias[0] == duzias[1] == duzias[2]:
        dz = duzias[0]
        duzias_restantes = [d for d in [1, 2, 3] if d != dz]
        return f"Os últimos 3 números estão na mesma dúzia ({dz}). Aposte nas dúzias {duzias_restantes}."

    return "Nenhuma recomendação. Os últimos 3 números não pertencem à mesma coluna nem à mesma dúzia."

def atualizar_lista(ultimos_numeros, novo_numero):
    """Atualiza a lista de números sorteados, mantendo apenas os 10 mais recentes."""
    ultimos_numeros.append(novo_numero)
    if len(ultimos_numeros) > 10:
        ultimos_numeros.pop(0)
    return ultimos_numeros

# Inicializa a lista com os 10 últimos números sorteados
ultimos_numeros = []

while True:
    print("\nÚltimos números sorteados:", ultimos_numeros)
    novo_numero = input("Digite o próximo número sorteado (ou 'sair' para encerrar): ")
    if novo_numero.lower() == 'sair':
        break

    if not novo_numero.isdigit():
        print("Por favor, insira um número válido.")
        continue

    novo_numero = int(novo_numero)
    if novo_numero < 0 or novo_numero > 36:
        print("Por favor, insira um número entre 0 e 36.")
        continue

    # Atualiza a lista de números e gera uma recomendação
    ultimos_numeros = atualizar_lista(ultimos_numeros, novo_numero)
    recomendacao = recomendar_aposta(ultimos_numeros)
    print(recomendacao)
