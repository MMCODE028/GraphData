from urllib import response
import requests 
import pandas as pd 
from sqlalchemy import column, create_engine
import requests
import pandas as pd
import pyodbc 
from datetime import date
import time
import uuid

today = str(date.today())

def colecting_data(df):
    url = 'https://data.exia.com.co/demo/data/last'
    try:
        response = requests.get(url).json()
    except Exception as e:
        print(404)
    else:
        print(200)
    
    data_id = str(uuid.uuid1(clock_seq=3))
    co2factor = response["co2factor"]
    createddata = response["created_at"].split(" ")
    created_at = "{}".format(today)
    created_at_time = createddata[3] 
    day_energy = response["day_energy"]
    id = response["id"]
    pac_sum = response["pac_sum"]
    pac_sum_counter = response["pac_sum_counter"]
    pac_sum_temp = response["pac_sum_temp"]
    power_counter = response["power_counter"]
    power_real = response["power_real"]
    power_real_temp = response["power_real_temp"]
    reference = response["reference"]
    total_energy = response["total_energy"]
    updatedata = response["update_at"].split(" ")
    update_at = "{}".format(today)
    update_at_time = updatedata[3]

    df = df.append({"data_id":data_id,"co2factor": co2factor,"created_at" : created_at,"created_at_time":created_at_time,"day_energy" : day_energy,
    "id" : id,"pac_sum" : pac_sum,"pac_sum_counter" : pac_sum_counter,"pac_sum_temp": pac_sum_temp,
    "power_counter": power_counter,"power_real": power_real,"power_real_temp": power_real_temp,"reference": reference,
    "total_energy":total_energy,"update_at": update_at, "update_at_time":update_at_time}, ignore_index = True)

    return df

df = pd.DataFrame(columns=[
    'data_id',
    'co2factor',
    'created_at',
    "created_at_time",
    'day_energy',
    'id',
    'pac_sum',
    'pac_sum_counter',
    'pac_sum_temp',
    'power_counter',
    'power_real',
    'power_real_temp',
    'reference',
    'total_energy',
    'update_at',
    'update_at_time'
    ])

df = colecting_data(df)

host = "ec2-54-204-56-171.compute-1.amazonaws.com"
db = "d8c2qn1cjpa6v5"
user = "egmmzxqrtpfjog"
pasw = "9f500321118b8732bf737f7aa02a4331affb585f9c187788de99cf2bbf7a6c69"

engine = create_engine('postgres://egmmzxqrtpfjog:9f500321118b8732bf737f7aa02a4331affb585f9c187788de99cf2bbf7a6c69@ec2-54-204-56-171.compute-1.amazonaws.com:5432/d8c2qn1cjpa6v5')
df.to_sql('lastdata', engine, if_exists='append')

