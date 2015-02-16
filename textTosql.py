
import os
import sys
import sqlite3


def cta_paginas (nombre_archivo,contador):
    with open(nombre_archivo,'r') as tempFile:
        archivo_completo = tempFile.readlines()
        # print archivo_completo
        for line in archivo_completo :
            if "NOMBRE" in line:
                contador += 1
                # contadorLineas = contadorLineas + 1
                # print line
                # print contador
            # contadorLineas = contadorLineas + 1

    # print contadorLineasl
    # print contador
    return contador


def cta_lineas (nombre_archivo,contador,pagina):
    with open(nombre_archivo,'r') as tempFile:
        rut_flag = True
        nom_flag = False
        cont_nombre = 0
        archivo_completo = tempFile.readlines()
        while rut_flag:
            for line in archivo_completo :
                print 'cNombre ' , cont_nombre
                print 'pagina ' , pagina
                print 'nom_flag ' ,  nom_flag
                print 'linea ' , line
                print 'contador ', contador
                print 'rut_flag ', rut_flag
                if "NOMBRE" in line:
                    cont_nombre += 1
                if "C.IDENTIDAD" in line and cont_nombre == pagina:
                    rut_flag = False
                    break
                if "NOMBRE" in line and cont_nombre == pagina:
                    nom_flag = True
                    continue
                if line.strip() and nom_flag:
                    contador += 1
                    # cont_nombre = cont_nombre + 1

    return contador


def inserta_sql(nombre_user, rut_user, dv_user, dir_user, file_actual):
    conn = sqlite3.connect('usuarios')
    c = conn.cursor()
    valores = [nombre_user, rut_user, dv_user, dir_user, file_actual]
    c.execute('INSERT INTO alfa VALUES (?,?,?,?,?)', valores,)
    conn.commit()
    conn.close()


def parse_rut (rut):
    rut = rut.split('-')
    ci = rut[0].replace(".", "")
    dv = rut[1]
    return ci, dv

# def llenaMatrizTemporal () :

cont = 0
cont2 = 0
pagina = 1
mi_rut = 0
mi_dv = ''
nuevaCuenta = 0
bandera = False

archivosLista = os.listdir("/home/francisco/PDF")

tempMatrix = [[] for _ in range(70)]

# tempMatrix =  [ [ range(5) ] for i in range(70) ]
# print tempMatrix
# tempMatrix[0].append("jose francisco")
# print tempMatrix
# tempMatrix[4].append(13212057)
# print tempMatrix
# for x in range(0,69)
# contador = cta_paginas("/home/francisco/PDF/A1249004.pdf.txt",cont)

contadorLineas = cta_lineas("/home/francisco/PDF/A1249004.pdf.txt", cont2, pagina)

# print contador
print 'pagina ',pagina,' lineas ', contadorLineas

mi_rut, mi_dv = parse_rut('13.212.057-k')
print mi_rut,mi_dv


with open("/home/francisco/PDF/A1249004.pdf.txt",'r') as tempFile:
    archivo_completo = tempFile.readlines()
    for linea in archivo_completo:
        if "NOMBRE" in linea and nuevaCuenta == 0:
            bandera = True
            continue

        if not bandera:
            continue

        if bandera:
            tempMatrix[nuevaCuenta].append(linea)
            nuevaCuenta += 1
            if nuevaCuenta > 69:
                break

print tempMatrix

# inserta_sql('jose francisco vergara',13212057,'9','eleuterio ramirez 875', 'A1249004')

# with open("/home/francisco/PDF/A1249004.pdf.txt",'r') as f:
#   data = f.readlines()
#   for linea in data:
#   print linea.rstrip('\n')  #quita el salto de linea al final de la linea