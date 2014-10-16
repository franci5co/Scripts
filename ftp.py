#!/usr/bin/python
import os
import ftplib
filename = "dumpdew.txt"
ftp = ftplib.FTP('10.37.1.20')
ftp.login('dewofr','dewofr')
ftp.cwd("/usr/sap/DEW/monitor")
localfile = open(filename, 'wb')
ftp.retrbinary('RETR ' + "dump.txt", localfile.write, 1024)
localfile.close()
ftp.quit()
archivo = open("/home/dm0adm/dumpdew.txt","r")
final = open("/home/dm0adm/dumpdew.tmp","w")
dato = archivo.read()
final.write(dato.strip()+'\n')
archivo.close()
final.close()
os.remove("/home/dm0adm/dumpdew.txt")
os.rename("/home/dm0adm/dumpdew.tmp", "/home/dm0adm/dumpdew.txt")