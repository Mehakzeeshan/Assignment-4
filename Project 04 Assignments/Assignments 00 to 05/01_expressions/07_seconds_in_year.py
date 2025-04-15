days_in_year: int = 365
hours_in_day: int = 24
minutes_in_hour: int = 60
seconds_in_minute: int = 60



def main():

    seconds_in_year: int = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
    print("There are", seconds_in_year, "seconds in a year.")
    
if __name__ == '__main__':
    main()