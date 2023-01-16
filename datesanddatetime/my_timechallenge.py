# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz
import random

# random_timezone_list = []
# timezone_list = []
timezone_list = sorted(pytz.all_timezones[25:35])
# len_tz_list = len(pytz.all_timezones)
choice = ''

while choice != '0':
    # upper_range = random.randint(0, len_tz_list)
    # for i in range(upper_range - 10, upper_range):
    #     random_timezone_list.append(pytz.all_timezones[i])
    # timezone_list = sorted(random_timezone_list)

    if choice in timezone_list:
        choice_zone = pytz.timezone(choice)
        time_zone_time = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(tz=choice_zone)
        local_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()
        print("Given time zone '{}' time is: {}\nLocal time is {}\nUTC time is {}".format(choice_zone,
                                                                                          time_zone_time,
                                                                                          local_time, utc_time))
    for index, zone in enumerate(timezone_list):
        print(index+1, zone, sep=':')
    print(0, 'To quit', sep=":")
    print()
    choice = input("Please select a valid choice from the timezone options above: ")


