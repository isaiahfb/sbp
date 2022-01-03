import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

URL = 'https://portal.rockgympro.com/portal/public/314b60a77a6eada788f8cd7046931fc5/occupancy?&iframeid=occupancyCounter&fId=1072'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

body = soup.find('body')

script = body.find('script')

string = str(script)

string = string[0:string.find('function')]

pop = string[string.find('POP'):string.find('UPW')]
upw = string[string.find('UPW'):string.find('FRE')]
fre = string[string.find('FRE'):] 

row = [str(datetime.now())]

for location in [pop, upw, fre]:
   location = location[location.find("'capacity' : ")+13:]
   row.append(location[:location.find(",")])
   location = location[location.find("'count' : ")+10:]
   row.append(location[:location.find(",")])
   location = location[location.find("(")+1:]
   row.append(location[:location.find(")")])

filename = "sbpdata.csv"

print(row)

with open(filename, 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    #csvwriter.writerow(["time", "pop_capacity", "pop_count", "pop_updated","upw_capacity", "upw_count", "upw_updated","fre_capacity", "fre_count", "fre_updated",])
    csvwriter.writerow(row)
