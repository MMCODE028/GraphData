import random 
from datetime import datetime 

Numero = 100
i = 0 

names = ['Santiago', 'Erick', 'Maria', 'Juan', 'Sebastian','Sergio','Carlos']

def select(names):
    return random.choice(names)


while(i<= Numero):
    inicio = datetime(2022,4,30)
    final = datetime(2022,5,27)

    random_date = inicio + (final - inicio) * random.random()
    
    print("Iteraccion Numero: ", i)
    print("Date: ", random_date, "Name: ", select(names))

    i=i+1




