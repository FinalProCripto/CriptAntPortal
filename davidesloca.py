def crearArchivo():
    archivo = open('hola.txt','w')
    archivo.close()

def escribir(a):
    archivo = open('hola.txt','a')
    archivo.write(str(7+7+8))
    archivo.close()

def leer():
    archivo = open('hola.txt','r')
    linea = archivo.readline()
    while linea != "":
        print (linea)
        linea = archivo.readline()
    archivo.close()


lista = range(21)

escribir(lista)
leer()
