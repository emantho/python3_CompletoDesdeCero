


def operaciones():
    pass

def suma(a=0 , b=0):
    # Filtro para evitar valores no numerivos
    try:
        if a == str() or b == str():
            raise TypeError ("Error: Tipo de dato no válido")
        return a + b
    
    except TypeError:
        print(f"Error: Tipo de dato no válido")

def resta(a=0 , b=0):
    try:
        if a == str() or b == str():
            raise TypeError ("Error: Tipo de dato no válido")
        return a - b
    
    except TypeError:
        print(f"Error: Tipo de dato no válido")

def producto(a=0 , b=0):
    try:
        if a == str() or b == str():
            raise TypeError ("Error: Tipo de dato no válido")
        return a * b
    
    except TypeError:
        print(f"Error: Tipo de dato no válido")

def division(a=0 , b=0):
    try:
        if a == str() or b == str():
            raise TypeError ("Error: Tipo de dato no válido")
        
        elif b == 0:
            raise ZeroDivisionError ("Error: No es posible dividir entre cero")

        else: 
            return a * b
    
    except TypeError:
        print(f"Error: Tipo de dato no válido")
    
    except:
        print(f"Error: No es posible dividir entre cero")



# para evitar ejecutar el codigo de un modulo desde otro fichero, utilizar una comprobación que devuelve el nombre del fichero mientras se ejecuta:
if __name__ == '__main__': # name en este caso contiene el nombre saludar cuando se ejecuta desde otro sitio. Si se ejecuta desde aquí mismo el nombre es main
    operaciones()

