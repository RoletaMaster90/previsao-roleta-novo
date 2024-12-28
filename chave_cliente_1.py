import sys

# Função para verificar se a chave inserida pelo cliente é válida
def verificar_chave(chave_esperada):
    chave_inserida = input("Digite sua chave de ativação: ")
    if chave_inserida != chave_esperada:
        print("Chave inválida. O programa será encerrado.")
        sys.exit()  # Encerra o programa caso a chave seja inválida
    else:
        print("Chave válida! O código será ativado.")

# Função principal do código de previsão de roleta
def main():
    # Chave única gerada para o Cliente (Exemplo: chave para o Cliente 1)
    chave_cliente_1 = "7028fad9-9094-4d60-87dd-63f48b2a5f48"  # Você pode modificar esta chave conforme necessário para cada cliente

    # Verificar a chave inserida pelo cliente
    verificar_chave(chave_cliente_1)
    
    # Aqui começa o código de previsão de roleta (adicione sua lógica da roleta aqui)
    print("Bem-vindo ao Código de Previsão de Roleta!")
    # Coloque o restante do código de previsão da roleta aqui...
    
    # Exemplo simples de roleta (substitua com a lógica real)
    while True:
        numero_sorteado = input("Digite o próximo número sorteado: ")
        print(f"Número sorteado: {numero_sorteado}")
        # Você pode adicionar a lógica do seu código de previsão da roleta aqui

if __name__ == "__main__":
    main()
