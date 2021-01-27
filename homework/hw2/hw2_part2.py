# this is the function
def time_to_seconds(hour,minute,second):
    time = hour*3600+minute*60+second
    return time
def calculate_years(a,b,c):
    years = (a-b)/c
    return years
    

# the main body 
current_day_length = time_to_seconds(23,56,4)
print("The current length of a day is {0} seconds.".format(current_day_length))

desired_day_length = int(input("Enter the desired day length in seconds => "))
print(desired_day_length)
print()
desired_hour = desired_day_length //(60*60)
desired_minute_length = desired_day_length %(60*60)
desired_minute = desired_minute_length//60
desired_second = desired_minute_length %60
changing_years = 900*1000000
changing_hours = 6
changing_rate = 6 * 60 * 60 / 900/1000000
expected_year = round(calculate_years(desired_day_length,current_day_length,changing_rate))+2018


# output
print("{0} seconds is a day length of {1} hours {2} minutes and {3} seconds.".format(desired_day_length,desired_hour,desired_minute,desired_second ))
print("A day change rate of {0} hours every {1} years, ".format(changing_hours,changing_years))
print("represents {:.6f} seconds per year.".format(changing_rate))
print("A day length of {1} hours, {2} minutes and {3} seconds,".format(desired_day_length,desired_hour,desired_minute,desired_second ))
print("Would be in year {0}".format(expected_year))