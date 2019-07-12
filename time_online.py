import requests
import re
import datetime

print("-------- TIME --------")


country = []

url = 'https://www.timeanddate.com/worldclock/'
url_google = 'https://www.google.com/'

country_name = input("Enter the name of the country: ")
country_name = country_name.lower()
first = country_name[0].upper()
country_name = first + country_name[1:]


city_name = input("Enter the name of the city: ")
city_name = city_name.lower()
first_s = city_name[0].upper()
city_name = first_s + city_name[1:]

#<div class="vk_bk dDoNo">5:11 AM</div>
#<span id="ct" class="h1">19:04:26</span>

req = requests.get(url + str(country_name) + "/" + str(city_name))
out = req.text

filtered = re.findall(r'..:..:..', out)    # THIS
if len(filtered) > 0:
    print("Current local time in {}, {} is\n {}".format(country_name, city_name, filtered))
else:
    print("Make sure you entered the info correctly")




#<div class="vk_bk dDoNo">5:11 AM</div>
#<span id="ct" class="h1">19:04:26</span>

