import requests
from bs4 import BeautifulSoup
import csv


def RankByColumn():
    for APweek in range(1, 1228):
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
"Arkansas",
"Arkansas State",
"Army",
"Auburn",
"Ball State",
"Baylor",
"Boise State",
"Boston College",
"Bowling Green",
"Buffalo",
"BYU",
"California",
"Central Michigan",
"Charlotte",
"Cincinnati",
"Clemson",
"Coastal Carolina",
"Colorado",
"Colorado State",
"Duke",
"East Carolina",
"Eastern Michigan",
"Florida Atlantic",
"FIU",
"Florida",
"Florida State",
"Fresno State",
"Georgia",
"Georgia Southern",
"Georgia State",
"Georgia Tech",
"Hawaii",
"Houston",
"Illinois",
"Indiana",
"Iowa",
"Iowa State",
"Jacksonville State",
"James Madison",
"Kansas",
"Kansas State",
"Kent State",
"Kentucky",
"Liberty",
"Louisiana",
"Louisiana–Monroe",
"Louisiana Tech",
"Louisville",
"LSU",
"Marshall",
"Maryland",
"Memphis",
"Miami (FL)",
"Miami (OH)",
"Michigan",
"Michigan State",
"Middle Tennessee",
"Minnesota",
"Mississippi State",
"Missouri",
"Navy",
"NC State",
"Nebraska",
"Nevada",
"New Mexico",
"New Mexico State",
"North Carolina",
"North Texas",
"Northern Illinois",
"Northwestern",
"Notre Dame",
"Ohio",
"Ohio State",
"Oklahoma",
"Oklahoma State",
"Old Dominion",
"Ole Miss",
"Oregon",
"Oregon State",
"Penn State",
"Pittsburgh",
"Purdue",
"Rice",
"Rutgers",
"Sam Houston",
"San Diego State",
"San Jose State",
"SMU",
"South Alabama",
"South Carolina",
"South Florida",
"Southern Miss",
"Stanford",
"Syracuse",
"TCU",
"Temple",
"Tennessee",
"Texas",
"Texas A&M",
"Texas State",
"Texas Tech",
"Toledo",
"Troy",
"Tulane",
"Tulsa",
"UAB",
"UCF",
"UCLA",
"UConn",
"UMass",
"UNLV",
"USC",
"UTEP",
"UTSA",
"Utah",
"Utah State",
"Vanderbilt",
"Virginia",
"Virginia Tech",
"Wake Forest",
"Washington",
"Washington State",
"West Virginia",
"Western Kentucky",
"Western Michigan",
"Wisconsin",
"Wyoming"

]

GenFlourishChart(teams, 1, 1227, "apranks.csv")



