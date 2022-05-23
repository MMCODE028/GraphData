from email.mime import application
from sqlite3 import apilevel
import pymysql
import os

from sympy import apart_list, sqf

class App:

    def __init__(self):
        
        self.conn = pymysql.connect(
            host = "casab.mysql.database.azure.com",
            user= 'casab001',
            password='CA765@19',
            database ='casabapidata')

        self.cursor = self.conn.cursor()

    
    def Mostrar(self):
        sql = "select * from lastdata"
        self.cursor.execute(sql)
        energy = self.cursor.fetchall()
        for i in energy:
            print("DataID:", i[0] , "Created:", i[2],"Time:",i[3], "EnergyT:", i[13], "update", i[15])

    def Guardar(self):
        energy = []
        sql = "select * from lastdata"
        self.cursor.execute(sql)
        lastdata = self.cursor.fetchall()
        for i in lastdata:
            print("EnergyT",i[13])
            energy.append(i[13])
        return energy


    def GuardarTime(self):
        Time = []
        sql = "select * from lastdata"
        self.cursor.execute(sql)
        lastdata = self.cursor.fetchall()
        for i in lastdata:
            print("Time",i[3])
            Time.append(i[3])
        return Time




application = App()
application.Mostrar()
#application.Guardar()
#application.GuardarTime()
#Lista = application.Guardar()
#listaTime = application.GuardarTime()
#print("Lista---------------------------------------------------")
#print(Lista)
print("Lista Time----------------------------------------------------")
#print(listaTime)






        
