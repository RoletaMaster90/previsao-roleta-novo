import os

# Chave de ativação válida (gerada por você para cada cliente)
CHAVE_VALIDA = "ABC123"  # Substitua por uma chave exclusiva para cada cliente

# Arquivo para registrar que o programa foi ativado
ARQUIVO_ATIVACAO = "ativado.txt"

# Verificar se o programa já foi ativado
def verificar_ativacao():
    return os.path.exists(ARQUIVO_ATIVACAO)

# Registrar a ativação no arquivo
def registrar_ativacao():
    with open(ARQUIVO_ATIVACAO, "w") as arquivo:
        arquivo.write("Programa ativado com sucesso!")

# Função principal
def main():
    if verificar_ativacao():
        print("Programa já ativado. Bem-vindo de volta!")
    else:
        print("Bem-vindo! Para usar o programa, insira sua chave de ativação.")
        chave = input("Digite sua chave de ativação: ").strip()
        if chave == CHAVE_VALIDA:
            registrar_ativacao()
            print("Chave válida! Programa ativado com sucesso.")
        else:
            print("Chave inválida. Entre em contato para obter uma chave válida.")
            exit()

    # Código principal do programa (exemplo)
    print("Iniciando o Programa de Previsão de Roleta...")
    # Adicione aqui o código funcional da roleta

# Executar o programa
if __name__ == "__main__":
    main()
