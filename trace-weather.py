import requests
import sys  #to change the exit code
zipcode=sys.argv[1]
countrycode=sys.argv[2]
apikey="2dc2f3f5fd48ae935ab09f3ce976a7bd"

weather_url= f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={apikey}"
result= requests.get(weather_url)

if result.status_code ==200:
    print(result.json())
    sys.exit(0)
else:
    print(f"Error: {result.json()['message']}")
    sys.exit(1)
