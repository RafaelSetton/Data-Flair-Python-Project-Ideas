from random import randint

num = randint(1, 99)
mini = 0
maxi = 100
tentativas = 0

while True:
    esc = int(input(f"Escolha um número entre {mini} e {maxi}: "))
    if esc > maxi or esc < mini:
        continue
    tentativas += 1
    if esc > num:
        maxi = esc
    elif esc < num:
        mini = esc
    elif esc == num:
        print(f'Parabéns você acertou o número {num} com {tentativas} tentativas!')
        break
    elif mini + 1 == num == maxi - 1:
        print(f"Você perdeu. O número {num} é o único restante")
