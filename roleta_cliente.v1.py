import uuid

# Função para obter o UUID único da máquina
def obter_uuid_maquina():
    """Retorna o UUID da máquina para garantir que o código só funcione nela"""
    return str(uuid.getnode())  # UUID único da máquina

# Função para verificar se o UUID é válido
def verificar_uuid(uuid_cliente):
    """Verifica se o UUID inserido corresponde ao UUID da máquina autorizada"""
    uuid_permitido = 'SEU_UUID_UNICO_AQUI'  # Substitua por um UUID válido gerado para o cliente
    if uuid_cliente != uuid_permitido:
        print("Este código não é válido para esta máquina. Por favor, entre em contato para obter uma versão válida.")
        return False
    return True

# Funções de obtenção da coluna e dúzia (como no código original)
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

# Código principal que será executado
if __name__ == "__main__":
    # Obter UUID da máquina
    uuid_maquina = obter_uuid_maquina()
    
    # Verificar se o UUID é válido
    if not verificar_uuid(uuid_maquina):
        exit()  # Se o UUID não for válido, o programa é encerrado

    # Loop para inserir os números e gerar recomendações
    numeros_sorteados = []
    print(f"Últimos números sorteados: {numeros_sorteados}")
    
    while True:
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
