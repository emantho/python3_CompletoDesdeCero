import sys

#print(sys.argv)
# La impresión de este argumento siempre es la ruta del script, al ser una lista este valor siempre va ser el index 0
#['/home/emanja/projects/python3_CompletoDesdeCero/Fase 2 - Manejo de datos y optimizacion/Tema 05 - Entradas y salidas de datos/hola.

for argumento in sys.argv[1:]:
    print(argumento)



