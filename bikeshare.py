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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ")
        city = city.lower()
        if CITY_DATA.get(city):
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
    while True:
        month = input('Enter the month you would like to view bikeshare data for (January, February, March, April, May, June, or all): ')
        month = month.lower()
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
    while True:
        day = input('Enter the day of week you would like to view bikeshare data for (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all): ')
        day = day.lower()
        if day in days:
            break

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
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f'Most popular month is: {popular_month}')

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f'Most popular day of week is: {popular_day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'Most popular hour is: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'Most commonly used start station is: {popular_start_station}')

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'Most commonly used end station is: {popular_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + ' AND ' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print(f'Most frequent combination of start station and end station is: {popular_start_end}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print(f'The total travel time is: {total_trip} seconds')

    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()
    print(f'The mean travel time is: {mean_trip} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        genders = df['Gender'].value_counts()
        print(genders)
    else:
        print("Gender data does not exist in this set.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        min_year = df['Birth Year'].min()
        print(f'The earliest year of birth is: {min_year}')
        max_year = df['Birth Year'].max()
        print(f'The most recent year of birth is: {max_year}')
        popular_year = df['Birth Year'].mode()[0]
        print(f'The most common year of birth is:: {popular_year}')
    else:
        print("Birth Year data does not exist in this set.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters() # Done
        df = load_data(city, month, day) # Done

        time_stats(df) # Done
        station_stats(df) # Done - check
        trip_duration_stats(df) # Done -check
        user_stats(df) # Done - check

        #TO DO - add a Q for if they would like to view raw data (5 rows at a time)  - Done
        raw_data = input('\nWould you like to view 5 rows of raw data? Enter yes or no: ').lower()
        if raw_data in ('yes', 'y'):
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                more_data = input('Would you like to see 5 more rows of raw data? Enter yes or no: ').lower()
                if more_data not in ('yes', 'y'):
                    break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
