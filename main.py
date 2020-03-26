#Import Dependencies
import requests
import json
#Import Local Files
from resources import myBuys as mb

baseUrl = "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name="
results = []

#Generate and sanitize url
for i, item in enumerate(mb.items):
    if item[0] == "":
        url = baseUrl + item[1] + item[0]
    else:
        url = baseUrl + item[1] + "%20" + "(" + item[0] + ")"

    url = url.replace(' ', '%20')    

#Make post request and extract data using json    
    post = json.loads(requests.post(url).text)
    	
    results.append([post['lowest_price'][:-1].replace(',', '.'), item[1] + " " + item[0], item[2]])

totalProfit = 0

for item in results:
    profit = round(float(item[0]) - float(item[2]), 2)
    print(f"You have made €{profit} on {item[1]}, current price is {round(float(item[0]), 2)}")
    totalProfit += profit

print(f"Your total profit is €{round(totalProfit,2)}")