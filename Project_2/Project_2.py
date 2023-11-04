import requests
from bs4 import BeautifulSoup
import csv


def RankByColumn(filename):
    for APweek in range(1, 12):
        AP_row = []
        url = f"https://collegepollarchive.com/football/ap/seasons.cfm?appollid={APweek}"
        r = requests.get(url)
        s = BeautifulSoup(r.content, "html5lib")
        week = s.select("title")
        weekTitle = week[0].text
        weekTitleFinal = weekTitle.replace("Football Polls | College Poll Archive", "")
        find_teams = s.select("a[href*=teamid]")
        AP_row.append(weekTitleFinal)
        for i in range(0, 25):
            try:
                AP_row.append(find_teams[i].text)
                #print(find_teams[i].text)
            except:
                break
        with open(filename, mode='a', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(AP_row)
        print(AP_row)


def GenerateDates():
    titles = []
    file2 = "date.csv"
    for APweek in range(1, 1227):
        url = f"https://collegepollarchive.com/football/ap/seasons.cfm?appollid={APweek}"
        r = requests.get(url)
        s = BeautifulSoup(r.content, "html5lib")
        week = s.select("title")
        weekTitle = week[0].text
        weekTitleFinal = weekTitle.replace("Football Polls | College Poll Archive", "")
        titles.append(weekTitleFinal)
    with open(file2, mode='a', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(titles)


def GenFlourishChart(FootballTeams, start, end, filename):
    bigboylist = []
    weeklylist = []
    for Team in FootballTeams:
        weeklylist.append(Team)
    bigboylist.append(weeklylist)
    for APweek in range(start, end + 1):
        url = f"https://collegepollarchive.com/football/ap/seasons.cfm?appollid={APweek}"
        r = requests.get(url)
        s = BeautifulSoup(r.content, "html5lib")
        find_teams = s.select("a[href*=teamid]")
        team_under_25 = len(find_teams) - 1
        weeklylist = []
        for Team in FootballTeams:
            for i in range(0, 25):
                print(f"Working on {Team}, week {APweek}, int {i}")
                try:
                    if (find_teams[i].text == Team):
                        weeklylist.append(i + 1)
                        break
                    elif (find_teams[i].text != Team and (i >= 24 or i >= team_under_25)):
                        weeklylist.append("")
                        break
                except:
                    break
        bigboylist.append(weeklylist)
    print(bigboylist)
    zippy = zip(*bigboylist)
    with open(filename, mode="a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(zippy)

teams = [
  
"Air Force",
"Akron",
"Alabama",
"Appalachian State",
"Arizona",
"Arizona State",


]

GenFlourishChart(teams, 1000, 1012, "apranks.csv")



