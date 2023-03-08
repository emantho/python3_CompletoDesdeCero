# se esta importando todas las funciones definidad en saludar()

# # import saludos

# # saludos.saludar()


# Para importar de forma selectiva se debe cambiar la forma de hacer el import

# si se tiene mas de una función se añaden usando comas luego del import saludar, otro, otro

# # from saludos import saludar

# tambien es posible importar todo usando *

# # from saludos import * # esto trae todos las definiciones pero carga más la memoria

# # saludar()

# # Saludo()


# Para importar un modulo dentro de un paquete se usa la siguiente sintaxis

from mensajes.hola.saludos import saludar, Saludo
from mensajes.adios.despedida import despedir, Despedida

saludar()
Saludo()

despedir()
Despedida()