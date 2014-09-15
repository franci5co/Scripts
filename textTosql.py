
import os
import sys
import sqlite3


def ctaPaginas (nombreArchivo,contador,contadorLineas):
	
	with open(nombreArchivo,'r') as tempFile:
		archivoCompleto = tempFile.readlines()
		#print archivoCompleto
		for line in archivoCompleto :
			if ("NOMBRE" in line):
				contador = contador + 1
				contadorLineas = contadorLineas + 1
				#print line
				#print contador
			else:
				contadorLineas = contadorLineas + 1

	print contadorLineas
	print contador
	return (contador, contadorLineas)

def insertaSQL (nombreUsuario,rutUsuario,dvUsuario,dirUsuario,archivoActual):
	conn = sqlite3.connect('/home/francisco/Documents/usuarios')
	c = conn.cursor()
	c.execute("INSERT INTO usuarios VALUES ('?','?','?','?','?')")
	conn.commit()
	conn.close()

#def llenaMatrizTemporal () :

cont = 0
cont2 = 0

archivosLista = os.listdir("/home/francisco/PDF")
tempMatrix = [[] for _ in range(70)]
#tempMatrix =  [ [ range(5) ] for i in range(70) ] 
#print tempMatrix 
#tempMatrix[0].append("jose francisco")
#print tempMatrix
#tempMatrix[4].append(13212057)
#print tempMatrix
#for x in range(0,69)
	
contador, contadorLineas = ctaPaginas("/home/francisco/PDF/A1249004.pdf.txt",cont,cont2)
print contador
print contadorLineas

#with open("/home/francisco/PDF/A1249004.pdf.txt",'r') as f:
#	data = f.readlines()
#	for linea in data:
		#print linea.rstrip('\n')  #quita el salto de linea al final de la linea