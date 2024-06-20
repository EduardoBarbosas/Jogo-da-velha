import random

def play():
    user = input("Insira: 'pedra', 'papel', ou 'tesoura'\n ")
    computer = random.choice(['pedra','papel','tesoura'])

    if user == computer:
     return 'É um empate!'
    
    if is_win(user, computer):
       return 'Você ganhou!'
    
    return 'Você perdeu!'
 
def is_win (jogador, oponente):
       if (jogador == 'pedra' and oponente == 'tesoura') or (jogador == 'tesoura' and oponente == 'papel') \
        or (jogador == 'papel' and oponente == 'pedra '):
          return True
       
print(play())