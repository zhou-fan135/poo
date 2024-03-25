import random
import time

class Personagem:
    def _init_(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.energia = 50

    def atacar(self, alvo):
        dano = random.randint(5, 15)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")
        return dano

    def habilidade_especial(self, alvo):
        pass

class Guerreiro(Personagem):
    def habilidade_especial(self, alvo):
        if self.energia >= 10:
            dano = random.randint(10, 20)
            alvo.vida -= dano
            self.energia -= 10
            print(f"{self.nome} usa habilidade especial em {alvo.nome} causando {dano} de dano!")
            return dano
        else:
            print(f"{self.nome} não tem energia suficiente para usar a habilidade especial!")
            return 0

class Arqueiro(Personagem):
    def habilidade_especial(self, alvo):
        if self.energia >= 8:
            dano = random.randint(8, 18)
            alvo.vida -= dano
            self.energia -= 8
            print(f"{self.nome} usa habilidade especial em {alvo.nome} causando {dano} de dano!")
            return dano
        else:
            print(f"{self.nome} não tem energia suficiente para usar a habilidade especial!")
            return 0

def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")
    classe = ''
    while classe not in ['Guerreiro', 'Arqueiro']:
        classe = input("Escolha uma classe (Guerreiro/Arqueiro): ")
        if classe not in ['Guerreiro', 'Arqueiro']:
            print("Classe inválida. Por favor, escolha 'Guerreiro' ou 'Arqueiro'.")
    if classe == 'Guerreiro':
        return Guerreiro(nome, classe)
    else:
        return Arqueiro(nome, classe)

print("Criação do Jogador 1:")
jogador1 = criar_personagem()
print("\nCriação do Jogador 2:")
jogador2 = criar_personagem()

while jogador1.vida > 0 and jogador2.vida > 0:
    jogador1.atacar(jogador2)
    jogador2.atacar(jogador1)
    jogador1.habilidade_especial(jogador2)
    jogador2.habilidade_especial(jogador1)
    print(f"\nStatus: {jogador1.nome} - Vida: {jogador1.vida}, Energia: {jogador1.energia}")
    print(f"Status: {jogador2.nome} - Vida: {jogador2.vida}, Energia: {jogador2.energia}\n")
    time.sleep(2)

if jogador1.vida > 0:
    print(f"{jogador1.nome} venceu a batalha!")
elif jogador2.vida > 0:
    print(f"{jogador2.nome} venceu a batalha!")
else:
    print("Ambos os jogadores caíram em batalha!")