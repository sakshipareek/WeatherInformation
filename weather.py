import requests
#import os
from datetime import datetime

api_key = '60745bb229a072b6a0063e08825bcbb9'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data["main"]['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


ans = input("Do you want to append in the file or write in a new one.\nType 'a' for append and 'w' for new file")
# to store the following in the text file
# here "a" will append the wheather stats everytime user runs this

if ans == 'a' or ans == 'A':
    with open(r"log.txt", "a") as f:
        f.write("\n\n-------------------------------------------------------------\n")
        f.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
        f.write("-------------------------------------------------------------\n")

        f.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
        f.write(f"Current weather desc  : {0}\n".format(weather_desc))
        f.write(f"Current Humidity      : {0}%\n".format(hmdt))
        f.write(f"Current wind speed    :{0} kmph\n".format(wind_spd))
elif ans == 'w' or ans == 'W':
    with open(r"log.txt", "w") as f:
        f.write("-------------------------------------------------------------\n")
        f.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
        f.write("-------------------------------------------------------------\n")

        f.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
        f.write(f"Current weather desc  : {0}\n".format(weather_desc))
        f.write(f"Current Humidity      : {0}%\n".format(hmdt))
        f.write(f"Current wind speed    :{0} kmph\n".format(wind_spd))


