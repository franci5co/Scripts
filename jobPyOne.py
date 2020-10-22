
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
#import SCRIPT.config


desde = "xxx"
para = "xxx"
estados = 'CANCELADO=A, TERMINADO=F, LIBERADO=S, PLANEADO=P, LISTO=Y, ACTIVO=R, DESCONOCIDO=X'
file = 'E:\\Monitor\\SCRIPT\\resJob.txt'
texto = "Reporte Jobs"

msj = MIMEMultipart('alternative')
msj['Subject'] = "ADPro: Reporte JOBS"
msj['From'] = desde
msj['To'] = para

proceso = subprocess.run('E:\\Monitor\\SCRIPT\\jobQuery.bat', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);

#print(proceso)

if proceso.returncode == 0 :
    retorno = 'OK'
    with open(file) as f:
        text = f.readlines()
        size = len(text)
        #print(size)
        f.close()
else:
    retorno = 'Error'


try:
    if size != 1 :
        mensajeHTML = pd.read_csv(file, dtype=str)
        mensajeHTML = mensajeHTML.to_html(justify='justify-all')
    else :
        mensajeHTML = '<h2>Sin jobs cancelados</h2>'
except pd.errors.EmptyDataError:
    mensajeHTML = '<h2>Error en query o en la ejecucion de jobs</h2>'
    #mensajeHTML = mensajeHTML.to_string()


#print(mensajeHTML)

mensajeHTML = "<h1>Reporte Jobs ADPro</h1>" + "<p> Ejecucion de Query Jobs = " +  retorno  + "</p>" + mensajeHTML + " " + "<p>"


parte1 = MIMEText(texto,'plain')
parte2 = MIMEText(mensajeHTML,'html')

msj.attach(parte1)
msj.attach(parte2)

mail = smtplib.SMTP('smtp.gmail.com:587')
mail.ehlo()
mail.starttls()
mail.login('xxx','xxx')
mail.sendmail(desde,para.split(','), msj.as_string())
mail.quit()



