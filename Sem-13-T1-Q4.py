listaPar = []
listaImpar = []
listaNumeros = []
numero = 0
for i in range(20):
    listaNumeros.append(int(input("")))
    numero = listaNumeros[i]
    if(numero%2 == 0):
 	    listaPar.append(numero)
    else:
 	    listaImpar.append(numero)

print(listaNumeros)
print(listaPar)
print(listaImpar)
