import requests as r
degree_sign = u"\N{DEGREE SIGN}"
city = input("Input cityname: ").capitalize()
data = r.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=58e87355d6592f9dfc975f414ba880a4')
json = data.json()
try: 
    print(f"Today in {city}:\nTemperature: {round(json['main']['temp']-273.15,2)}{degree_sign}C\nMin Temperature: {round(json['main']['temp_min']-273.15,2)}{degree_sign}C\nMax Temperature: {round(json['main']['temp_max']-273.15,2)}{degree_sign}C")
except:
    print("Wrong cityname was given.")
