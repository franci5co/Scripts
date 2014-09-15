
import os
import sys
import sqlite3


def ctaPaginas (nombreArchivo,contador):
	
	with open(nombreArchivo,'r') as tempFile:
		archivoCompleto = tempFile.readlines()
		#print archivoCompleto
		for line in archivoCompleto :
			if ("NOMBRE" in line):
				contador = contador + 1
				#contadorLineas = contadorLineas + 1
				#print line
				#print contador
			#contadorLineas = contadorLineas + 1

	#print contadorLineasl
	#print contador
	return contador

def ctaLineas (nombreArchivo,contador,pagina):
	
	with open(nombreArchivo,'r') as tempFile:
		rutFlag = True
		nomFlag = False
		contNombre = 0
		archivoCompleto = tempFile.readlines()
		while (rutFlag):
			for line in archivoCompleto :
				print 'cNombre ' , contNombre
				print 'pagina ' , pagina
				print 'nomFlag ' ,  nomFlag
				print 'linea ' , line
				print 'contador ', contador
				print 'rutFlag ', rutFlag
				if ("NOMBRE" in line):
					contNombre = contNombre + 1
				if ("C.IDENTIDAD" in line and contNombre == pagina):
					rutFlag = False
					break
				if ("NOMBRE" in line and contNombre == pagina):
					nomFlag = True
					continue
				if (line.strip() and nomFlag):
					contador = contador + 1
				#contNombre = contNombre + 1

	return contador

def insertaSQL (nombreUsuario,rutUsuario,dvUsuario,dirUsuario,archivoActual):
	conn = sqlite3.connect('usuarios')
	c = conn.cursor()
	valores = [nombreUsuario,rutUsuario,dvUsuario,dirUsuario,archivoActual]
	c.execute('INSERT INTO alfa VALUES (?,?,?,?,?)', valores,)
	conn.commit()
	conn.close()

def formateaRUT (rut):
	rut = rut.split('-')
	ci = rut[0].replace(".","")
	dv = rut[1]
	return (ci,dv)

#def llenaMatrizTemporal () :

cont = 0
cont2 = 0
pagina = 16
mi_rut = 0
mi_dv = ''

archivosLista = os.listdir("/home/francisco/PDF")

tempMatrix = [[] for _ in range(70)]

#tempMatrix =  [ [ range(5) ] for i in range(70) ] 
#print tempMatrix 
#tempMatrix[0].append("jose francisco")
#print tempMatrix
#tempMatrix[4].append(13212057)
#print tempMatrix
#for x in range(0,69)
	
contador = ctaPaginas("/home/francisco/PDF/A1249004.pdf.txt",cont)
contadorLineas = ctaLineas("/home/francisco/PDF/A1249004.pdf.txt", cont2, pagina)

print contador
print 'pagina ',pagina,' lineas ', contadorLineas

mi_rut, mi_dv = formateaRUT('13.212.057-k')
print mi_rut,mi_dv
##insertaSQL('jose francisco vergara',13212057,'9','eleuterio ramirez 875', 'A1249004')

#with open("/home/francisco/PDF/A1249004.pdf.txt",'r') as f:
#	data = f.readlines()
#	for linea in data:
		#print linea.rstrip('\n')  #quita el salto de linea al final de la linea