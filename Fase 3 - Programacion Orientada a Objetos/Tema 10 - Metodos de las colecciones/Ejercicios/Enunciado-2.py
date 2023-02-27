# Completa el ejercicio aquí
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(lista):

    lista_2 = lista[:]
    # Borrar los elementos duplicados
    lista_2 = list(set(lista_2))

    # Ordenar la lista de mayor a menor
    lista_2.sort(reverse=True)
    print(lista_2)
    
    # Eliminar todos los números impares
    lista_3 = []
    for i in lista_2:
        if i % 2 == 0:
            lista_3.append(i)
    
    lista_2 = lista_3[:]
    print(lista_2)

    


modificar(lista)