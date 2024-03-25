import random
from time import sleep
from tqdm import tqdm

nome = input("Digite aqui o seu nome: ")
sleep(1)
print(f"Prazem em te conhecer {nome}!")
sleep(2)

def desenho_gato():
    print("  /\\_/\\")
    print(" / o o \\")
    print("(   \"   )")
    print(" \\~(*)~/")

def numero_sorteado(min, max):
    numero = random.randint(int(min),int(max))
    return numero

game = True

while game == True:
    print("Vamos jogar um game para tentar adivinhar um numero sorteado aleatóriamente, gostaria de jogar?")
    print("Sim (1)")
    print("Não (2)")
    opcao = int(input(""))
    if opcao == 1:
        print("Opa, bora!")
        sleep(2)
        print("Um momento por favor, sorteando o número")
        for i in tqdm(range(20)):
            sleep(0.1)
        print("Pronto, agora tente adivinhar, lembrando que o número está entre 1 e 10")
        sleep(2)
        numeroSorteado = numero_sorteado(1,10)
        
        acertou = False
        while acertou == False:
            opcao_player = int(input("Sua opção: "))
            if opcao_player != numeroSorteado:
                print("ERROU!")
            elif opcao_player == numeroSorteado:
                print("ACERTOU!")
                sleep(2)
                print(f"PARABENS {nome}! AQUI SEU PRÊMIO!")
                sleep(1)
                desenho_gato()
                sleep(1)
                acertou = True
                

    elif opcao == 2:
        print("Sem problemas, podemos jogar depois!")
        game = False
        