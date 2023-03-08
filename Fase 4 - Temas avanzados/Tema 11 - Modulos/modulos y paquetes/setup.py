from setuptools import setup

setup(
    name='Mensajes',
    version='1.1',
    description='Un paquete para saludar y despedir',
    author='Eder Manjarres',
    author_email='hola@ktaca.dev',
    url='https://www.ktaca.dev',
    package=['mensajes','mensajes.hola','mensajes.adios'],
    scripts=['test.py']
)


# Luego de armar la plantilla antes indicada se debe realizar los siguientes pasos:

# 1) Para crear el paquete
#   Desde la CLI ejecutar -> python3 setup.py sdist
#   Esto generará un paquete comprimido en el mismo directorio
#   y un archivo .egg-info
# 
# 2) Para instalar el paquete:
#   Ubicar el directorio donde está el paquete comprimido e instalar usando pip (o mover a directorio de destino)
#   pip install <paquete>.tar.gz (linux) .zip (windows)
#   Al ejecutar se creará un archivo con el nombre del paquete en el directorio indicado
#       
#   Con "pip list" es posible ver la lista de paquetes instalados

# 3) Para actualizar
#   Repetir el paso 1 cambiando el número de versión
#   Cambiar el mensaje si se quiere
#   Repetir paso 2 apuntando a la nueva versión añadiendo --upgrade al final, ie. pip install <paquete>.tar.gz --upgrade
#   

# 4) Para desinstalar
#   pip uninstall <paquete> ie. pip uninstall mensajes
#

