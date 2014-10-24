#lets make the years. This will contain years from 1901 to 2000
#lets make all the year as a list.
#every seven day make a week

dayInWeek = 2
numberOfSundayFirstOfTheMonth = 0
for i in range(1901,2001):
    #lets make months
    for j in range(1, 13):

        #Thirty days has September, April, June and November.
        if j in [4,6,9,11]:
            numbersOfDay = 30
        #  February has twenty-eight, And on leap years, twenty-nine.
        #  A leap year occurs on any year evenly divisible by 4,
        # but not on a century unless it is divisible by 400.
        elif j in [2]:
            if i%4 == 0 or (i%400):
                numbersOfDay = 29
            else:
                numbersOfDay = 28
        else:
            numbersOfDay = 31

        for day in range(1,numbersOfDay+1):
            if dayInWeek == 7 and day == 1:
                numberOfSundayFirstOfTheMonth+= 1
            dayInWeek+=1
            if dayInWeek == 8:
                dayInWeek = 1


print(numberOfSundayFirstOfTheMonth)
