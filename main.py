input_month = str(input())
input_day = int(input())

#Check the Winter season

if (input_month == 'January') and (1 <= input_day <= 31):
    print('Winter')
elif (input_month == "February") and (1 <= input_day <= 29):
    print('Winter')
elif (input_month == "March") and (1 <= input_day <= 19):
    print('Winter')
elif (input_month == "December") and (1 <= input_day <= 31):
    print('Winter')

#Check the Spring season
elif (input_month == 'March') and (20 <= input_day <= 31):
    print('Spring')
elif (input_month == "April") and (1 <= input_day <= 30):
    print('Spring')
elif (input_month == "May") and (1 <= input_day <= 31):
    print('Spring')
elif (input_month == "June") and (1 <= input_day <= 20):
    print('Spring')

#Check the Summer season
elif (input_month == 'June') and (21 <= input_day <= 30):
    print('Summer')
elif (input_month == "July") and (1 <= input_day <= 31):
    print('Summer')
elif (input_month == "August") and (1 <= input_day <= 30):
    print('Summer')
elif (input_month == "September") and (1 <= input_day <= 21):
    print('Summer')

#Check the Autumn season.
elif (input_month == 'September') and (22 <= input_day <= 30):
    print('Autumn')
elif (input_month == 'October') and (1 <= input_day <= 31):
    print('Autumn')
elif (input_month == 'November') and (1 <= input_day <= 30):
    print('Autumn')
elif (input_month == 'December') and (1 <= input_day <= 20):
    print('Autumn')
#Check if the string and int are valid (an actual month and day)
else:
    print('Invalid')
