lista =[9.8,10,7,9.9,8.5,7.9,9.3,9,6,8.7,8.2,8.9,9.4,8.7,6.7]
n = len(lista)
swapped = True
while swapped:
     swapped = False
     for i in range(n-1):
        if lista[i] > lista[i+1]:
            lista[i],lista[i+1] = lista[i+1], lista[i]
            swapped=True

print("Lista ascendente",lista)

swapped = True
while swapped:
     swapped = False
     for i in range(n-1):
        if lista[i] < lista[i+1]:
            lista[i],lista[i+1] = lista[i+1], lista[i]
            swapped=True

print("lista descendente",lista)