import requests
import os
from datetime import datetime
user_api=os.environ['api_key']
location=input("enter the location =>")
complete_api_link=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
api_link=requests.get(complete_api_link)
api_data=api_link.json()
print(api_data)
if api_data['cod']=='404':
    print("Invalid_city :{}, please check the city name correctly !!")
else:    
 temp_city= (api_data['main']['temp']-273.15)
 weather_desc=api_data['weather'][0]['description']
 hmdt= api_data['main']['humidity']
 wind_spd =api_data['wind']['speed']
 date_time=datetime.now().strftime("%d %b %Y | %I : %M: %S %p")

 print("_______________________________________________________")
 print("Weather stats for -{}||{}".format(location.upper(),date_time))
 print("_______________________________________________________")

 print("current temperature is :{:.2f} deg C ".format(temp_city))
 print("current weather description :",weather_desc)
 print("current humidity :",hmdt,'%')
 print("current wind speed :",wind_spd,'KMPH')






