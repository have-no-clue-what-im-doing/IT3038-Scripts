import requests
from bs4 import BeautifulSoup

url = "https://collegepollarchive.com/football/ap/seasons.cfm?appollid=1" #I can iterate through the AP Poll ID, starting from 1 and going all the way 1 thousand something.

r = requests.get(url)

s = BeautifulSoup(r.content, "html5lib")

#find_table = s.find_all("table", {"class": "table table-sm table-hover w-auto"})
week = s.select("title")
print(week[0].text)

find_team = s.select("a[href*=teamid]") #having that teamid makes this a million times easier. Otherwise I'd have to navigate through a stupid amount of table tags. 

#I can make this a function and put the rank variable in there. Might use this as my next project and iterate through every single AP poll ever. 
print(find_team[25].text)


rank = 1 
for team in find_team:
    print(f"{rank} {team.text}")
    rank += 1
    if rank >= 26: #Top 25 only. A lot of the tables will have un-ranked teams that I do not want. 
        break
