import requests

api_key = '909782e83fa293e28538f4b35da6db59'

userInput = input("Enter the city name:\n") 
weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=imperial&APPID={api_key}')

if weather_data.json()['cod'] == '404':
    print(f"Invalid city name.")

else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather of {userInput} is {weather}.\n")
    print(f"The temperature of {userInput} is {temp}.")