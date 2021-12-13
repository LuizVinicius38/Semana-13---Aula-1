lista = []
n = input("Digite um número, para adicionar na lista! ")
lista.append(n[::-1])
print(lista)

n = 0
lista = []
while n < 2:
    nota = float(input("Digite a nota! "))
    lista.append(nota)
    n = n + 1
    media = sum(lista) / len(lista)
    if nota == 0:
        print("SEM NOTAS")
        pass
print("Nota: {}" .format(nota))
print("Média: {}" .format(media))


separarPalavra = []
vogais = []
n = 0
while n < 2:
    palavra = str(input("Digite um palavra! "))
    for i in palavra:
        separarPalavra.append(i)
        if i in "a":
            vogais.append(i)
            separarPalavra.remove(i)
        elif i in "e":
            vogais.append(i)
            separarPalavra.remove(i)
        elif i in "i":
            vogais.append(i)
            separarPalavra.remove(i)
        elif i in "o":
            vogais.append(i)
            separarPalavra.remove(i)
        elif i in "u":
            vogais.append(i)
            separarPalavra.remove(i)
    n = n + 1    
    print("Consoantes: {}" .format(separarPalavra))
    print("Vogais: {}" .format(vogais))
    print("Quantidade de vogais: {}" .format(len(vogais)))
    #Limpa a Lista
    separarPalavra.clear()
    vogais.clear()   
