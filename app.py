# vamos instalar o rich para fazer prints com cores: 
# pip install rich
from rich import print
import os

# Variáveis
votos_b, votos_l = 0, 0

# loop eterno
while True:
    # apresente os candidatos
    print('*'*20)
    # usando [on blue] e [on red] da biblioteca rich
    print(f'[on blue]TOTAL BOLSONARO:[/]{votos_b}{os.linesep}[on red]TOTAL LULA: [/]{votos_l}')
    print('*'*20)

    # permita votar usando try e except para que o código não quebre durante a execução
    try:
        # usamos o {os.linesep} para fazer uma quebra de linha no terminal
        voto = int(input(f'para quem gostaria de votar?{os.linesep}17 - Bolsonaro{os.linesep}13 - Lula{os.linesep}seu voto: '))
        if voto == 17:
            votos_b += 1
        elif voto == 13:
            votos_l += 1
        else:
            pass

    except:
        print('Digite apenas 13 ou 17')

    # agora vamos apagar o terminal a cada reload usando 'csl' no terminal para dar clear
    os.system('cls') 
    
