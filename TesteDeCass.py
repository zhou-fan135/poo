class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone


pessoas = []


def registrar():
    nome = input("qual o nome da pessoa: ")
    cpf = input("qual o cpf da pessoa: ")
    telefone: str = input("qual o numero da pessoa: ")
    return Pessoa(nome, cpf, telefone)


def visualizar(contato):
    b = input("digite o nome da pessoa que deseja encontrar: ")
    for p in pessoas:
        if p.nome == b:
            return p
    return None

def deletar():
    c = input("digite o nome da pessoa que deseja deletar: ")



while True:
    a = input("para registrar uma nova pessoa digite 1\npara visualizar as informações uma pessoa digite 2"
              "\npara deletar uma pessoa digite 3\npara editar uma pessoa da lista digite 4: ")
    if a == '1':

        pessoa = registrar()
        pessoas.append(pessoa)
        print("pessoa registrada ")
    elif a == '2':
        while True:
            pessoa = visualizar(pessoa)
            if pessoa != None:
                break
            print("Pessoa não encontrada. Tente novamente.")
        print(pessoa.__dict__)
    elif a == '3':
        pass
    elif '4':
        break
    else:
        pass



