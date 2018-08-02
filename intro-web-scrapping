from bs4 import BeautifulSoup
import requests
import json
import urllib

search = input("Enter the search keyword.")
# parameters = {'q':search}
# r = requests.get("https://www.google.com/search", params = parameters )
#
# soup = BeautifulSoup(r.text)
# # print(soup.prettify())
#
# results = soup.find("div", {"class": "ksBKIe g"})
#
# links = results.findAll("div", {"class": "IvtMPc"})
#
# for item in links:
#     item_text = item.find("span").text
#
#     print(item_text)


API_KEY = "AIzaSyBg8jd710Kzq2kPUWEQFFs6vcb14LRIZ"

parameters = {'input':search, 'key': API_KEY}

r = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json", params = parameters )

newDictionary = json.loads(r.text)

for singlePlace in newDictionary["results"]:
    print("Name: ", singlePlace['name'])
    print("Rating: ", singlePlace['rating'])
    print("Address: ", singlePlace['formatted_address'])
    print("*******************************************")
