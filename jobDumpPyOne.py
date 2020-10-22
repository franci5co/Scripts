
import pandas as pd
import contextlib
import os
import sys
import smtplib
import re
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess



desde = "xxx@xxx.xxx"
para = "xxx"
file = 'E:\\Monitor\\SCRIPT\\resDump.txt'

texto = "Reporte Dumps"

proceso = subprocess.run('E:\\Monitor\\SCRIPT\\dumpQuery.bat', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);

print(proceso)

if proceso.returncode == 0 :
    retorno = 'OK'
    with open(file) as f:
        text = f.readlines()
        size = len(text)
        print(size)
        f.close()
else:
    retorno = 'Error'

try:
    if size != 1 :
        mensajeHTML = pd.read_csv(file, dtype=str)
        mensajeHTML = mensajeHTML.to_html(justify='justify-all')
        #print("hola")
    else :
        mensajeHTML = '<h2>Sin dumps</h2>'
except pd.errors.EmptyDataError:
    mensajeHTML = '<h2>Error en query o en la ejecucion de jobs</h2>'
    #mensajeHTML = mensajeHTML.to_string()

msj = MIMEMultipart('alternative')
msj['Subject'] = "ADPro: PRD Reporte " + str(size-1) + " Dumps"
msj['From'] = desde
msj['To'] = para

mensajeHTML = "<h1>Reporte Dumps ADPro = " + str(size-1) + "</h1>" + "<p> Ejecucion de Query Dumps = " +  retorno  + "</p>" + mensajeHTML

#print(mensajeHTML)

parte1 = MIMEText(texto,'plain')
parte2 = MIMEText(mensajeHTML,'html')

#print(msj)
msj.attach(parte1)
msj.attach(parte2)
#print(msj)
mail = smtplib.SMTP('smtp.gmail.com:587')
mail.ehlo()
mail.starttls()
mail.login('xxx','xxxx')
mail.sendmail(desde,para.split(','), msj.as_string())
mail.quit()



