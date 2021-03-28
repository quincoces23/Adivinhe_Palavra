# Jogo para adivinhar a palavra

from time import sleep

from desenhos import trofeu, morte

palavra_secreta = 'PORCO'

resposta = ''

tentativas = 0

print('-=-' * 9)

print('Descubra a palavra secreta!\nPrimeira Dica:\nÉ um animal!')

print('-=-' * 9)

while resposta != palavra_secreta:
    print(f'Tentativas até agora = {tentativas}')
    tentativas += 1
    resposta = input('Qual é a palavra secreta?:')
    resposta = resposta.upper().replace(' ', '')
    if resposta != palavra_secreta:
        print(f'Errou, {resposta} não é a palavra!')
        print('-=-' * 10)
    if resposta != palavra_secreta and tentativas >= 2 and tentativas != 7:
        sleep(1)
        print('Segunda dica: Se trata de um animal de fazenda.')
        print('-=-' * 15)
    if resposta != palavra_secreta and tentativas >= 4 and tentativas != 7:
        sleep(1)
        print('Terceira dica: Esse animal têm 4 patas.')
        print('-=-' * 15)
    if resposta != palavra_secreta and tentativas >= 6 and tentativas != 7:
        sleep(1)
        print('Quarta e ultima dica: Esse animal faz Oinc Oinc.')
        print('-=-' * 15)
    if resposta != palavra_secreta and tentativas >= 7:
        print('Número de tentativas explodiu.')
        morte()
        break
    if resposta == palavra_secreta and tentativas == 1:
        sleep(1)
        print(f'Parabéns!! você acertou a palavra!\n'
              f'Você precisou de {tentativas} tentativa.')
        trofeu()
    elif resposta == palavra_secreta and tentativas > 1:
        sleep(1)
        print(f'Parabéns!! você acertou a palavra!\n'
              f'Você precisou de {tentativas} tentativas.')
        trofeu()
