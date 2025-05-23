###################################
# Created by Owen Phillips        #
# Coding with Python Lab 2.2      #
# Using Variables                 # 
# Northwood Tech College          #
###################################


# Step 1

FirstName = 'Owen'
FavoriteDayOfWeek = 'Friday'
DaysInWeek = 7
HoursInDay = 24
MinutesInHour = 60
SecondsInMinute = 60
CostItem1 = 15
CostItem2 = 24
CostItem3 = 8
# Step 2

HoursInWeek = (DaysInWeek * HoursInDay)
SecondsInHour = (SecondsInMinute * MinutesInHour)
MinutesInDay = (MinutesInHour * HoursInDay)
TotalCost1_2 = (CostItem1 + CostItem2)
TotalCost2_3 = (CostItem2 + CostItem3)
TotalCost1_2_3 = (CostItem1 + CostItem2 + CostItem3)
# Step 3

print(MinutesInHour == SecondsInMinute)
print(CostItem1 >= CostItem3)
print(MinutesInHour < HoursInDay)
print(CostItem2 < DaysInWeek)
# Step 4

print(str(HoursInWeek))
print(str(SecondsInHour))
print(str(TotalCost2_3))
# Step 5

print('Hello ',FirstName,'! Did you know that there are ',str(MinutesInDay),' minutes in a day and ',HoursInWeek,' hours in a week?', sep='')
print('I went shopping on ',FavoriteDayOfWeek,' and spent $',TotalCost1_2_3,'! The first two items were only $',TotalCost1_2,sep='',end='.')
