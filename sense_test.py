from sense_hat import SenseHat
from time import sleep
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
import numpy as np
from dateutil import tz
from datetime import datetime, timedelta


def PlotData(x, data):
    trace1 = go.Scatter(x=x, y=data[0,:], name='Temperature')
    trace2 = go.Scatter(x=x, y=data[1,:], name='Pressure')
    trace3 = go.Scatter(x=x, y=data[2,:], name='Humidity')
    plotdata = [trace1, trace2, trace3]

    fig = tools.make_subplots(rows=3, cols=1)
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace3, 3, 1)
    fig.append_trace(trace2, 2, 1)
    
    py.plot(fig, filename='Coldframe', auto_open=False)



#plotly.tools.set_credentials_file(username='nlbutts', api_key='T2uRt0ueu7ETyryt4yMWlr1c37zw81')

sense = SenseHat()

sense.set_rotation(180)

x    = []
temp = []
pres = []
hum  = []

counter = 0

utc = datetime.now()
cdt = utc - timedelta(hours=5)     

print(utc)
print(cdt)

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    utc = datetime.now()
    cdt = utc - timedelta(hours=5)     

    msg = "Date = {0}, Temperature = {1}, Pressure = {2}, Humidity = {3}".format(cdt, t,p,h)
    print(msg)

    x.append(cdt)
    temp.append(t)
    pres.append(p)
    hum.append(h)

    dt = np.array(x)
    y1 = np.array(temp)
    y2 = np.array(pres)
    y3 = np.array(hum)

    sleep(60)
    counter = counter + 1
    #msg = "{0}".format(counter)
    #sense.show_message(msg)
    if (counter >= 60):
        data = np.vstack((y1,y2,y3))
        print("Sending plot to PlotLy")
        PlotData(dt, data)
        counter = 0
