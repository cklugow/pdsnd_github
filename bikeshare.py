import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ["chicago", "new york", "washington"]
months = ["january", "february", "march", "april", "may", "june", "all"]
days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
df = None

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Which data would you like to analyze: chicago, new york or washington? ").lower()
        if city in cities:
            print("alright")
        else:
            print('Looks like you made a spelling mistake - please try again')
        break
    else:
            print("Please select from chicago, new york, or washington")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to analyze- january, february, march, april, may, june or all? ").lower()
        if month in months:
            print("alright")
        break
    else:
            print("Sorry!Please select from all or one month from january, february, march, april, may, june")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day would you like to analyze - monday, tuesday, wednesday, thursday, friday, saturday, sunday or all? ").lower()
        if day in days_of_week:
            print("alright")
        break
    else:
            print("Sorry!Please name one weekday or all")

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
    city_file = CITY_DATA[city]
    df = pd.read_csv(city_file)
    df = pd.DataFrame(df)
    print(city, city_file)
    print('-'*40)

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)
    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['weekday'] = df['Start Time'].dt.weekday
    popular_weekday = df['weekday'].mode()[0]
    print('Most Popular Start weekday:', popular_weekday)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination = df['Start Station'] + ' to ' + df['End Station']
    print('The most common start and end station is', Combination.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    mean_travel = df['Trip Duration'].sum()
    print("The total of trip duration is", mean_travel)

    # TO DO: display mean travel time
    total_travel = df['Trip Duration'].mean()
    print("The mean of trip duration is", total_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        counts_user_types = df['User Type'].value_counts()
        print("The counts_user_types is")
    for i in range(len(counts_user_types.index.values)):
        print(counts_user_types.index.values[i], ' : ', list(counts_user_types)[i])
    else:
        print("More user Type Data is not available")

    # TO DO: Display counts of gender
    counts_gender = df['Gender'].value_counts()
    print("The counts_gender is:")
    for i in range(len(counts_gender.index.values)):
        print(counts_gender.index.values[i], ' : ', list(counts_gender)[i])
    else:
        print("More Gender Data not available")

    # TO DO: Display earliest, most recent, and most common year of birth
    # earliest year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print("The earliest_year of birth is", int(earliest_year))

    # most recent year of birth
        most_recent_year = df['Birth Year'].max()
        print("The most_year of birth is", int(most_recent_year))

    # most common year of birth
        most_common_year = df['Birth Year'].mode()
        print("The most_common_year of birth is", int(most_common_year))
    else:
        print("Birth Year Data not available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    "Asks user to display the first 5 data rows"

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input('Do you wish to continue?: ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
