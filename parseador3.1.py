#!/usr/bin/python
import os
contador = 0
sc = 0
archivos = filter(os.path.isfile, os.listdir(os.curdir))
archivoout = open('salida.csv', 'w')
archivolog = open('archivos_procesados.txt', 'w')
for f in archivos:
    ruta_archivo = os.curdir
    path_archivo = os.getcwd()
    if ".py" not in f and ".csv" not in f:
        archivolog.write(f + "\n")
        with open(path_archivo + "/" + f, 'r') as origen:
            for linea in origen:
                contador += 1
                #  print linea
                if "Scanning" in linea:
                    sc = 1
                    url = linea.split()
                if "CMS" in linea and sc == 1:
                    sc = 0
                    cms = linea.split()
                    if cms[2] == "|":
                        ver = cms[1] + cms[2] + cms[3]
                    else:
                        ver = cms[1]
                    url1 = url[1].replace("...", "").replace("\x1b[m", "").replace("\x1b", "").replace("[0m", "")
                    cms1 = cms[0].replace("\x1b[m", "").replace("\x1b", "").replace("[0m", "")
                    archivoout.write(url1 + ";" + cms1 + ";" + ver + "\n")

archivoout.close()
archivolog.close()


