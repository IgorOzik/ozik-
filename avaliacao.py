avaliacao1 = int(input('Digite sua nota na primeira prova: '))
avaliacao2 = int(input('Digite sua nota na Segunda Avaliação: '))
notafinal = (avaliacao1 + avaliacao2) / 2

if notafinal >= 6 :
    print(f'Parabens campeão! Você conseguiu ser aprovado! sua media foi {notafinal}')
elif notafinal < 6:
    print(f'Reprovado, Banido! sua media foi {notafinal}')
