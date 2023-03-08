def despedir():
    print('Hola me despido desde despedida.despedir()')


class Despedida:
    def __init__(self):
        print("Adios, me despido desde Despedida.__init__()")





# para evitar ejecutar el codigo de un modulo desde otro fichero, utilizar una comprobación que devuelve el nombre del fichero mientras se ejecuta:


if __name__ == '__main__': # name en este caso contiene el nombre saludar cuando se ejecuta desde otro sitio. Si se ejecuta desde aquí mismo el nombre es main
    saludar()

