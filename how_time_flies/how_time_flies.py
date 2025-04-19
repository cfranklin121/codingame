import sys
import math

begin = input().split(".")
end = input().split(".")

long_months = [1, 3, 5, 7, 8, 10, 12]
short_months = [4, 6, 9, 11]

years = int(end[2]) - int(begin[2])
months = int(end[1]) - int(begin[1])
day_total = 0

month_start = int(begin[1])
month_tracker = []

leap_days = 0

#Get total years and months
if months < 0:
    years = years - 1
    months = 12 + months

for i in range(months):
    month_tracker.append(month_start)
    if month_start >= 12:
        month_start -= 12
    month_start += 1

#Get total days
for i in range(months):
    if month_tracker[i] in long_months:
        day_total += 31
    elif month_tracker[i] in short_months:
        day_total += 30
    elif int(end[2]) % 4 == 0:
        day_total += 29
    else:
        day_total += 28

#Calculate extra days for leap years
if int(begin[1]) <= 2:
    year_track = int(begin[2])
else:
    year_track = int(begin[2]) + 1

for i in range(int(end[2]) - year_track):
    if year_track % 4 == 0:
        leap_days += 1
    year_track += 1
    i += 1
    
days = int(end[0]) - int(begin[0])
if days < 0:
    months -= 1
days = days + day_total + (years * 365) + leap_days

#Output--------------------------------
if years == 1:
    print(f"{years} year,", end=" ")
elif years > 1:
    print(f"{years} years,", end=" ")

if months == 1 and days <= 30:
    pass
elif months == 1:
    print(f"{months} month,", end=" ")
elif months > 1:
    print(f"{months} months,", end=" ")

if days == 1:
    print(f"total {days} day")
elif days > 1 or days <= 0:
    print(f"total {days} days")