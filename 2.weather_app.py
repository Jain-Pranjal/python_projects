import requests
import json
# we are getting the weather data using web scrapping 
city=input("Enter the name of city : ")

url="https://www.codewithharry.com"  #link to an API
r=requests.get(url)  #making the connectiion with the url 
html_content=r.content  # getting the html form the url 
# print(html_content)

weather_dict=json.loads(html_content)
print(weather_dict)


# INCOMPLETE 