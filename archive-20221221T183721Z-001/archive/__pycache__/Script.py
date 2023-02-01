import os
import time
import pyautogui
import write
import archive

file = "gamesave.txt"

if not archive.FileExists(file):
    archive.CreateFile(file)

def cc(msg):
    for l in msg:
        pyautogui.press(l)
        time.sleep(0.0)
def wait():
    """
    Apenas um timer que espera 3 segundos e mostra na tela um novo ponto, indicando a passagem de tempo.
    """

    for t in range(0, 4):
        time.sleep(1)
        print(".", end="", flush=True)

def linha_c(msg):
    t = len(msg) + 2
    print("-"*t)
    print(f" {msg} ")
    print("-"*t)


def level_1():

    archive.WriteFile(file, "L1")
    linha_c("Nossa aventura começa, quando um jovem decide fazer alguma coisa: ")
    print("[1] Trabalhar")
    print("[2] Estudar")
    print("[3] Jogar")

    escolha_1 = int(input("O que ele vai fazer? "))
    
    if escolha_1 == 1:
        print("Parece que nosso protagonista é um homem de verdade!")

        time.sleep(3)
        os.system("clear")

        linha_c(f"Sua alternativa anterior foi: {escolha_1}")
        print("Continuando nossa jornada...")
        cc(f"Certo dia nosso amigo {personagem['Nome']}, estava trabalhando como de costume...")
        print()
        cc("So que nosso protagonista nao sabia o que lhe aguardava...")
        print()
        input("→ ")
        write.linha(20)

        os.system("clear")
        cc(f"{personagem['Nome']}, trabalhava em uma mineradora, desde seu menor aprendiz...")
        print()
        input("→ ")

        os.system("clear")
        cc(f"So que nesse dia em especifico, {personagem['Nome']} tinha uma sensacao diferente, pela primeira vez em anos se sentiu feliz em ir trabalhar...")
        print()
        input("→ ")

        os.system("clear")
        cc("Chegando la, percebeu que o dia estava maravilhoso, deslumbrante. E rapidamente comecou a trabalhar. Mas sua felicidade se torna medo quando ouve uma explosao na mina ao lado, e entao corre para ver o que aconteceu.")
        print()
        input("→ ")

    elif escolha_1 == 2:
        print("Provavelmente nosso protagonista é um nerd.")
        time.sleep(3)
        os.system("clear")
        linha_c(f"Sua escolha anterior foi: {escolha_1}")
        cc("Assim como qualquer outro dia. Nosso protagonista estava estudando, mas para que?")
        print()
        input("→ ")
        write.linha(20)
        read = archive.ReadFile(file)
        print(read)

    elif escolha_1 == 3:
        print("Então nosso protagonista parece ter uma vida, um tanto quanto depressiva...")
        time.sleep(3)
        os.system("clear")
        linha_c(f"Sua alternativa anterior foi: {escolha_1}")

    elif escolha_1 == 0:
        write.linha(30)
        write.caracter(personagem)

    


#Tutorial
os.system("clear")

while True:

    try:
        linha_c("Bem-vindo ao meu jogo de aventura!")
        print("[1] Opção 1")
        print("[2] Opção 2")
        print("[3] Opção 3")
        escolha_t = int(input("Você deseja: "))
        if escolha_t > 3:
            print("As escolhas são enumeradadas, por favor escolha um número dentro das opções")
            print("Tente escolher algo dentro das opções!")
            wait()
            os.system("clear")
            continue
        else:
            print("Esse tipo de escolha se repetirá durante todo o jogo!")
        
            entendeu = str(input("Você entendeu? [S/N]")).upper()
            if entendeu == "N":
                denovo = input("Vamos denovo então! (Pressione ENTER para continuar)")
                os.system("clear")
                continue
                
            elif entendeu == "S":
                break
    except:
        print("Por favor escolha as opções corretamente.")
        wait()
        os.system("clear")
        

    

    

print("Você passou do Tutorial!!")
time.sleep(3)
os.system("clear")

#Escolha do personagem:

personagem = dict()
write.caracter(personagem)


while True:
    write.linha(25)
    for k,v in personagem.items():
        print(f"Seu pesonagem tem: {k} - {v}")

    correto = str(input("Estamos certos quanto a isso? [S/N] ")).upper()

    if correto in "NÃONONOPEN":
        print("Vamos refazer então...")
        time.sleep(2)
        os.system("clear")
        write.caracter(personagem)

    elif correto in "SIMSSIYES":
        break
    
continua = input("Pressione ENTER para continuar.")
os.system("clear")

###########
# Estória #
###########


level_1()