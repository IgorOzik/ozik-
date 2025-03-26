qtdatual = int(input('Digite a quantidade atual do estoque de * produto da sua loja: '))
qtdminima = int(input('Digite a quantidade minima do estoque de * produto da sua loja: '))
qntmedia = (qtdatual + qtdminima) / 2

if qtdatual >= qntmedia:
    print(f'não efetuar a compra! quantidade media é {qntmedia}')
else:
    print(f'Efetue a Compra quantidade, media é {qntmedia}')
