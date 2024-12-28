import uuid

def obter_uuid():
    return str(uuid.getnode())  # Obtém o UUID baseado no endereço MAC da máquina

print("UUID da sua máquina é:", obter_uuid())
