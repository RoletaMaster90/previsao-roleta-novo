import uuid

# UUID da máquina do cliente
uuid_permitido = '5f8002ec-c3f6-11ef-810b-58ce2aed9e7c'  # Altere para o UUID correto da sua máquina


# Gerando o UUID da máquina atual
uuid_maquina = str(uuid.uuid1())

# Mostrando o UUID da máquina do cliente
print(f"UUID da sua máquina é: {uuid_maquina}")

# Solicitando que o cliente insira o UUID de ativação
uuid_ativacao = input("Digite o seu UUID de ativação: ")

# Comparando o UUID da máquina com o UUID de ativação
if uuid_ativacao == uuid_permitido:
    print("UUID válido! Acesso liberado.")
    
    # Aqui você pode colocar o código do programa que deve rodar se o UUID for válido
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
        """Sugerir apostas com base nos últimos números sorteados."""
        if len(numeros) < 2:
            return "Insira pelo menos 2 números para gerar uma recomendação."
        
        # Verificar se os últimos dois números estão na mesma coluna e/ou mesma dúzia
        coluna_ultimos = [obter_coluna(num) for num in numeros[-2:]]
        duzia_ultimos = [obter_duzia(num) for num in numeros[-2:]]
        
        recomendacao = []
        
        # Verificar coluna
        if coluna_ultimos[0] == coluna_ultimos[1]:
            recomendacao.append(f"Os últimos 2 números estão na mesma coluna ({coluna_ultimos[0]}). Aposte nas colunas ")
            # Sugerir colunas alternativas
            colunas_possiveis = [1, 2, 3]
            colunas_possiveis.remove(coluna_ultimos[0])
            recomendacao.append(f"{colunas_possiveis}.")
        else:
            recomendacao.append("Os últimos 2 números não estão na mesma coluna.")
        
        # Verificar dúzia
        if duzia_ultimos[0] == duzia_ultimos[1]:
            recomendacao.append(f"Os últimos 2 números estão na mesma dúzia ({duzia_ultimos[0]}). Aposte nas dúzias ")
            # Sugerir dúzias alternativas
            duzias_possiveis = [1, 2, 3]
            duzias_possiveis.remove(duzia_ultimos[0])
            recomendacao.append(f"{duzias_possiveis}.")
        else:
            recomendacao.append("Os últimos 2 números não estão na mesma dúzia.")
        
        return " ".join(recomendacao)

    # Loop para inserir os números e gerar recomendações
    numeros_sorteados = []

    while True:
        print(f"Últimos números sorteados: {numeros_sorteados}")
        numero = input("Digite o próximo número sorteado (ou 'sair' para encerrar): ")
        
        if numero.lower() == 'sair':
            break
        
        try:
            numero = int(numero)
            numeros_sorteados.append(numero)
            
            # Manter apenas os últimos 10 números sorteados
            if len(numeros_sorteados) > 10:
                numeros_sorteados.pop(0)
            
            print(sugerir_apostas(numeros_sorteados))
        except ValueError:
            print("Por favor, insira um número válido.")
else:
    print("UUID inválido! Acesso negado.")
