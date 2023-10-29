import requests
from bs4 import BeautifulSoup

url = "https://collegepollarchive.com/football/ap/seasons.cfm?appollid=1004" #I can iterate through the AP Poll ID, starting from 1 and going all the way 1 thousand something.

r = requests.get(url)

s = BeautifulSoup(r.content, "html5lib")

#find_table = s.find_all("table", {"class": "table table-sm table-hover w-auto"})
week = s.select("title")
print(week[0].text)

find_team = s.select("a[href*=teamid]") #having that teamid makes this a million times easier. Otherwise I'd have to navigate through a stupid amount of table tags. 

#I can make this a function and put the rank variable in there. Might use this as my next project and iterate through every single AP poll ever. 
rank = 1 
for team in find_team:
    print(f"{rank} {team.text}")
    rank += 1
    if rank >= 26: #Top 25 only. A lot of the tables will have un-ranked teams that I do not want. 
        break


'''
Example Output:
December 6, 2009 Football Polls | College Poll Archive
1 Alabama
2 Texas
3 TCU
4 Cincinnati
5 Florida
6 Boise State
7 Oregon
8 Ohio State
9 Georgia Tech
10 Iowa
11 Penn State
12 Virginia Tech
13 LSU
14 Miami (FL)
15 BYU
16 Oregon State
17 Pittsburgh
18 West Virginia
19 Stanford
20 Nebraska
21 Oklahoma State
22 Arizona
23 Utah
24 Wisconsin
25 Central Michigan
'''

#print(find_team[0].text)

