from datetime import date
from datetime import datetime

today = date.today()

def GetCurrentDate():
    currentMonth = int(today.strftime("%m"))
    currentDay = int(today.strftime("%d"))
    currentYear = int(today.strftime("%Y"))
    currentDateArray = [currentMonth, currentDay, currentYear]
    return currentDateArray

#I was going to do this by scratch but gave up. I screwed up big time on it. Calculations are totally different depending on whether your birthday month is before or after the current date

def SecondsOld(month, day, year):
    currentDate = GetCurrentDate()
    yearsOld = currentDate[2] - year
    print(yearsOld)

    def CalcDays(month, day):
        if month == 1:
            monthDays = 0
        if month == 2:
            monthDays = 31 #f leap years. not doing that
        if month == 3:
            monthDays = 59
        if month == 4: 
            monthDays = 90
        if month == 5:
            monthDays = 120
        if month == 6:
            monthDays = 151
        if month == 7:
            monthDays = 181
        if month == 8:
            monthDays = 212
        if month == 9:
            monthDays = 243
        if month == 10:
            monthDays = 273
        if month == 11:
            monthDays = 304
        if month == 12:
            monthDays == 334
        totalMonthPlusDays = monthDays + day
        return totalMonthPlusDays
    monthAndDayTotal = CalcDays(month, day)
    yearsOldInDays = yearsOld * 365
    totalDaysOld = yearsOldInDays + monthAndDayTotal
    TotalSecondsOld = totalDaysOld * 86400
    return TotalSecondsOld



#This is the final submission of code: datetime function takes 3 arguments: year, month, and day. It finds the difference between today and the birthday and returns the total number of days. I then used the .total_seconds() method to convert days into seconds       
print((datetime.now() - datetime(1984, 7, 8)).total_seconds())


