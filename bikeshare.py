import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }

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
    # city = input("enter city name : ").lower()
    while True:
        city = input("Kindly choose a city\n ch for 'chicago',\n ny for 'new york city'\n w for 'washington'\nto display the desired statistics: ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Oops! invalid selection; please try again.")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter a month from\n Jan\n feb\n mar\n apr\n may\n jun\nor type "all" to display all months: ').lower()
        MONTH_DATA = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']  
        if month in MONTH_DATA:
            break
        else:
            print('Please enter valid month name: ')     
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please enter a day from\n sat\n sun\n mon\n tue\n wed\n thu\n fri\nor "all" to show all days: ').lower()
        days = ['all', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri']
        if day in days:
            break
        else:
            print('Please enter valid day name')
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
   
    df = pd.read_csv(CITY_DATA[city])
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.startswith(day.title())]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month: ", most_common_month)

    # display the most common day of week
    day_name = df['day_of_week'].mode()[0]
    print("The most common day of week: ", day_name)
    # display the most common start hour
    df['hour'] = df["Start Time"].dt.hour
    start_hour = df['hour'].mode()[0]
    print('The most common start hour: ', start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most commonly used End station: ', end_station)

    # display most frequent combination of start station and end station trip
    start_end_station = start_station + ' ' + end_station
    print("Most frequent combination of start station and end station trip: ", start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)  
       
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration = df["Trip Duration"].sum()
    print("Total travel time: ", trip_duration)

    # display mean travel time
    mean_trip_duration = df["Trip Duration"].mean()
    print("Mean travel time: ", mean_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print('Counts of user types: ', user_types)

    # Display counts of gender
    # user_gender = df["Gender"].value_counts()
    # print("counts of gender", user_gender)
    try:
        user_gender = df['Gender'].value_counts()
        print("Counts of gender", user_gender)
    except:
        print("\nThere is no 'Gender' column in this file.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df["Birth Year"].min())
        most_recent = int(df["Birth Year"].max())
        most_common_year = int(df["Birth Year"].mode()[0])
        print("Earliest year of birth is: ", earliest)
        print("Most recent year of birth is:", most_recent)
        print("Most common year of birth: ", most_common_year)
    except:
        print("\nThere is no 'birth Year' column in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
def display_raw_data(city):
    df = pd.read_csv(CITY_DATA[city])
    
    print('\nRaw data is available to check... \n')
    start_loc = 0
    while True:
        display_opt = input('To display the availbale raw data in chuncks of 5 rows type: Yes, No \n').lower()
        if display_opt not in ['yes', 'no']:
            print('That\'s invalid choice, pleas type yes or no')

        elif display_opt == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5

        elif display_opt == 'no':
            print('\nExiting...')
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
   
