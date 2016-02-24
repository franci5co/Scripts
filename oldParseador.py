#!/usr/bin/python

ruta_archivo = "/home/francisco/Descargas/004_ipvulnerablesdetalle.txt"
contador = 0
lista1 = []
with open(ruta_archivo,'r') as origen:
    for line in origen:

        if "Heartbleed" in line:
            print line
            separado = line.partition("[1;31m")
	   # separadotest = separado[0].replace("\x1b[1m ","").replace("\x1b[m","").replace("\x1b","")
           # print separado
           # print separadotest + "separadotest"
	    lista1.append(separado)
            contador += 1
        if "Certificate Expiration" in line:

            separado = line.partition("[1;31m")

            lista1.append(separado)
            contador += 1
        if "Testing now" in line:

            separado = line.partition("--->")

            lista1.append(separado)
            contador += 1
        if "Service detected" in line:

            separado = line.partition(":")

            lista1.append(separado)
            contador += 1

#for index in range(len(lista1)):

    #print lista1[index]
    #print "indice numero " + str(index)



ruta_archivo_d = "/home/francisco/Descargas/004_ipvulnerablesSalida.txt"
#print lista1[contador-1]
testing = lista1[0][0].replace("[7m","").replace("[m","").replace("[1;31m","").replace("\x1b[1m ","").replace("\x1b[m","").replace("\x1b","").strip('\t\n\r')
testing2 = lista1[0][2].replace("[7m","").replace("[m","").replace("[1;31m","").replace("<---","").replace("\x1b[m","").replace("\x1b","").strip('\t\n\r')
certificado = lista1[2][0].replace("[1m","").replace("[m","").replace("[1;31m","").replace("\x1b[m","").replace("\x1b","").strip('\t\n\r')
certificado2 = lista1[2][2].replace("[1m","").replace("[m","").replace("[1;31m","").replace("\x1b[m","").replace("\x1b","").strip('\t\n\r')
heartbleed = lista1[3][0].replace("[1m","").replace("[m","").replace("[1;31m","").replace("\x1b[m","").replace("\x1b","").strip('\t\n\r')
heartbleed2 = lista1[3][2].replace("[1m","").replace("[m","").replace("[1;31m","").replace("\x1b[m","").replace("\x1b","").strip('\t\n\r')
service = lista1[1][0].lstrip().rstrip().strip('\t\n\r')
service1 = lista1[1][2].lstrip().rstrip().strip('\t\n\r')
#print heartbleed2+"hola"
#print testing
print testing
with open(ruta_archivo_d,'w') as destino:
    destino.write(testing.lstrip().rstrip()+";"+testing2.lstrip().rstrip()+";"+
                  service+";"+service1+";"+certificado.rstrip().lstrip()+";"+certificado2.rstrip().lstrip()+";"+
                  heartbleed.rstrip().lstrip()+";"+heartbleed2.rstrip().lstrip())
