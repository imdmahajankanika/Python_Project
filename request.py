import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={"Hour": 0.695652, "Temperature(°C)": 0.512381, "Humidity(%)": 0.622449, "Wind speed (m/s)": 0.837209, "Visibility (10m)": 0.678480, "Solar Radiation (MJ/m2)": 0.245690, "Rainfall(mm)": 0.0, "Snowfall (cm)": 0.0, "Seasons": 0.333333, "Holiday": 0.0, "Functioning Day": 0.0, "Year": 0.0, "Month": 0.272727, "Day": 0.466667})

print(r.json())

