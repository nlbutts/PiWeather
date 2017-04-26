from sense_hat import SenseHat
from time import sleep
from dateutil import tz
from datetime import datetime, timedelta
from pandas import DataFrame, read_csv
import pandas as pd
import os.path


sense = SenseHat()

t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()
#t = 1
#p = 2
#h = 3
t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

utc = datetime.now()
cdt = utc - timedelta(hours=5)

msg = "Date = {0}, Temperature = {1}, Pressure = {2}, Humidity = {3}".format(cdt, t,p,h)
print(msg)


dataFile = '/home/pi/projects/sense/sense_hat_data.csv'
if os.path.isfile(dataFile):
    df = pd.read_csv(dataFile)
    date=[cdt]
    temp=[t]
    pres=[p]
    hum=[h]
    DataSet = list(zip(date, temp, pres, hum))
    df2 = pd.DataFrame(data=DataSet, columns=['Date', 'Temperature_degC', 'Pressure_mbar', 'Humitity_percent'])
    df=df.append(df2)
    df.to_csv(dataFile, index=False)
else:
    date=[cdt]
    temp=[t]
    pres=[p]
    hum=[h]
    DataSet = list(zip(date, temp, pres, hum))
    df = pd.DataFrame(data=DataSet, columns=['Date', 'Temperature_degC', 'Pressure_mbar', 'Humitity_percent'])
    df.to_csv(dataFile, index=False)


samples = df['Date'].count()
pixels_lit = (samples % 64)

pixel_list=[]

for i in range(0, 64):
    if i < pixels_lit:
        pixel_list.append([255,255,0])
    else:
        pixel_list.append([0,0,0])
print(pixel_list)
sense.set_pixels(pixel_list)
sense.set_rotation(0)
