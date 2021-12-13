populacao = int(input(""))
a = populacao +(populacao -(10/100))
cont = 0
ano = 1600
for i in range(populacao, a):
    nascimento = populacao+(populacao +(1/100))
    mortes = populacao+(populacao +(6/100))
    ano = ano + 1
    cont = cont + 1
    if a <= populacao:
        print(f'{ano},{nascimento},{mortes},{populacao}')

    
                      
