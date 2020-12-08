import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    for city in CITY_DATA:      
            city=input("please enter city name(chicago,new york city,washington) or exit to leave:").lower()            
            if city=="chicago":
                print("here's Chicago")
                chicago=pd.read_csv("chicago.csv")
                break
                
            elif city=="new york city":
                print("You picked New York City")
                new_york_city=pd.read_csv("new_york_city.csv")
                break
                
            elif city=="washington":
                 print("You picked Washington")
                 washington=pd.read_csv("washington.csv")
                 break
                
            elif city=="exit":
                exit()
            else:
                print("\nPlease use one of the provided cities(chicago,new york city,washington\n")
                get_filters()
                

    # get user input for month (all, january, february, ... , june)no
    def month():
        while True:
            month=input("please enter a month from january to june or \'all\', or \'change\' to switch cities:").lower()
            if month=="january":
                print("\nSo you picked January\n")
                break
            
            elif month=="february":
                print("\nSo you picked February\n")
                break
        
            elif month=="march":
                print("\nSo you picked March\n")
                break
        
            elif month=="april":
                print("\nSo you picked April\n")
                break
            elif month=="may":
                print("\nSo you picked May\n")
                break
        
            elif month=="june":
                print("\nSo you picked June\n")
                break
            elif month=="change":
                print("\nlet's change cities then.\n")
                get_filters()
            elif month=="all":
                print("you chose all of the months")
                break
                return city, month, day
            else:
                print("Please choose a valid month")
    month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Enter day of the week or all,\'change month\' to modify month choice or \'change cities\' to start over from cities:").lower()
        if day=="sunday":
            print("you chose Sunday")
            break
            return city, month, day
        elif day=="monday":
            print("you chose Monday")
            break
            return city, month, day
        elif day=="tuesday":
            print("you chose Tuesday")
            break
            return city, month, day
        elif day=="wednesday":
            print("you chose Wednesday")
            break
            return city, month, day
        elif day=="thursday":
            print("you chose Thursday")
            break
            return city, month, day
        elif day=="friday":
            print("you chose Friday")
            break
            return city, month, day
        elif day=="saturday":
            print("you chose Saturday")
            break
            return city, month, day
        elif day=="change cities":
             print("\nlet's change cities then.\n")
             get_filters()
        elif day=="all":
            print("you chose all of the days in the week")
            break
            return city, month, day
            
        elif day=="change month":
            print("\ngoing back to month choices,please choose a month\n")
            month()
                  
        else:
             print("Please choose a valid day.hint(Sunday,Monday,ect..)")
 

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    data=input("Do you wish to see raw data?").lower()
    if data == 'yes':
        rows=len(df.index)
        while data=="yes":
            try:
                i=int(input("Type in the row number you wish to start with.With 0 being the first number: "))
                print(df.iloc[i:i+5,  :])
                i+=5
                if i>=rows:
                    print("That's all the data you viewed")
                    break
            except:
                if data!="no" or data!="yes":
                    print("\nPlease avoid letters or floats\n")
                
            try:    
                data=input("Do you wish to see other 5 rows?").lower()
                if data=="yes":
                    i=int(input("Type in the row number you wish to continue with: "))
                    print(df.iloc[i:i+5,  :])
                    i+=5
                elif data=="no":
                    break
            except ValueError:
                if data!="no" or data!="yes":
                    print("\nPlease avoid letters or floats\n")


             
             
             

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    count=0
    
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["month"]=df["Start Time"].dt.month
    common_month = df['month'].mode()[0]
    print("the most common month is : ",common_month)


    
    # display the most common day of week
    df["day_of_the_week"]=df["Start Time"].dt.dayofweek
    common_day_of_week=df["day_of_the_week"].mode()[0]
    print("\nthe most common day of the week is: ",common_day_of_week)
    




    # display the most common start hour
    df["hour"]=df["Start Time"].dt.hour
    common_hour=df["hour"].mode()[0]
    print("\nthe most common start hour is: ",common_hour)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_station=df["Start Station"].mode()[0]
    print("\nthe most commonly used start station is:{}\n".format(Start_station))



    # display most commonly used end station
    End_station=df["End Station"].mode()[0]
    print("Most common end station used is: ",End_station)


    # display most frequent combination of start station and end station trip
    Start_and_End=df["Start Station"] + "TO" +df["End Station"]
    print("\nthe most frequently used combination of both ends are: ",Start_and_End)
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_time=df["Trip Duration"].sum()
    print("The total travel time is: ",Total_time)


    # display mean travel time
    Mean_time=df["Trip Duration"].mean()
    print("The mean of the travel time is:{}".format(Mean_time))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\nUser type counts:{} \n".format(df["User Type"].value_counts()))
        


    # Display counts of gender
    try:
        print("\nGender counts:{} \n".format(df["Gender"].value_counts()))
    except KeyError:
            handler_1=input("washington doesn't contain gender data.Type in \'skip\' or \'change cities\' to start over: ").lower()
            if handler_1=="skip":
                pass
            elif handler_1=="change cities":
                print("\nlet's change cities then.\n")
                get_filters()
            else:
                print("that's not one of the provided options")
                


    # Display earliest, most recent, and most common year of birth
    try:
        print("the most earliest common year of birth is:{}".format(df["Birth Year"].mode()[0].max()))
    except:
            handler_2=input("washington doesn't contain year data.type \'skip\' to move on  or \'change cities\' to start over: ").lower()
            if handler_2=="skip":
                pass
            elif handler_2=="change cities":
                print("\nlet's change cities then.\n")
                get_filters()
            else:
                print("that's not one of the provdied options")
                      
        
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
