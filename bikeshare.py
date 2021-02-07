import pandas as pd
import numpy as np
import time
import math

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {  'january': 1,
                'february': 2,
                'march': 3,
                'april': 4,
                'may': 5,
                'june': 6}

WEEK_DATA = {   'monday': 0,
                'tuesday': 1,
                'wednesday': 2,
                'thursday': 3,
                'friday': 4,
                'saturday': 5,
                'sunday': 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        print("Please choose the city. ")
        city = input("Enter Chicago/ch, New York/ny or Washington/wa? ").lower()
        print()
        if city == 'ch':
            city = 'chicago'
        if city == 'ny':
            city = 'new york'
        if city == 'wa':
            city = 'washington'
        if city not in CITY_DATA:
            print('Please enter a valid city.')
            continue
        city = CITY_DATA[city]
        break


    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while 1:
        filter = input('Do you want to filter your data by month, day, both or none? ').lower()
        print()
        if filter =='month':
            print('Which month\'s data to show? ')
            month = input('Please enter jan, feb, mar, apr, may or jun". ').lower()
            print()
            if month == 'jan':
                month = 'january'
            if month == 'feb':
                month = 'february'
            if month == 'mar':
                month = 'march'
            if month == 'apr':
                month = 'april'
            if month == 'jun':
                month = 'june'
            if month not in MONTH_DATA:
                print('Sorry, invalid input. Let\'s try again. ')
                continue
            month = MONTH_DATA[month]
            day = 'all'
        elif filter == 'day':
            print('What is the day of the week to show? ')
            day = input('Please enter a short name like mon, tue, wed, thur, fri, sat or sun. ').lower()
            print()
            if day == 'mon':
                day = 'monday'
            if day == 'tue':
                day = 'tuesday'
            if day == 'wed':
                day = 'wednesday'
            if day == 'thur':
                day = 'thursday'
            if day == 'fri':
                day = 'friday'
            if day == 'sat':
                day = 'saturday'
            if day == 'sun':
                day = 'sunday'

            if day not in WEEK_DATA:
                print('Sorry, invalid input. Let\'s try again. ')
                continue
            day = WEEK_DATA[day]
            month = 'all'
        elif filter == 'both':
            print('Which month\'s data to show?')
            month = input('Please enter jan, feb, mar, apr, may or jun". ').lower()
            print()
            if month == 'jan':
                month = 'january'
            if month == 'feb':
                month = 'february'
            if month == 'mar':
                month = 'march'
            if month == 'apr':
                month = 'april'
            if month == 'jun':
                month = 'june'
            if month not in MONTH_DATA:
                print('Sorry, invalid input. Let\'s try again! ')
                continue
            month = MONTH_DATA[month]
            print('What is the day of the week to show?.')
            day = input('Please enter a short name like mon, tue, wed, thur, fri, sat or sun. ').lower()
            print()
            if day == 'mon':
                day = 'monday'
            if day == 'tue':
                day = 'tuesday'
            if day == 'wed':
                day = 'wednesday'
            if day == 'thur':
                day = 'thursday'
            if day == 'fri':
                day = 'friday'
            if day == 'sat':
                day = 'saturday'
            if day == 'sun':
                day = 'sunday'
            if day not in WEEK_DATA:
                print('Sorry, invalid input. Let\'s try again! ')
                continue
            day = WEEK_DATA[day]
        elif filter == 'none':
            day = 'all'
            month = 'all'
        else:
            print('Sorry, invalid input. Let\'s try again!')
            continue
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

    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    for num in MONTH_DATA:
        if MONTH_DATA[num] == common_month:
            common_month = num.title()
    print('Most Common Month is', common_month)

    # TO DO: display the most common day of week
    common_dow = df['day_of_week'].mode()[0]
    for num in WEEK_DATA:
        if WEEK_DATA[num] == common_dow:
            common_dow = num.title()
    print('Most Common Day of the Week is', common_dow)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour is', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    freq_combination = df['Start Station'] + " to " + df['End Station']


    # TO DO: display most commonly used start station
    print('Most commonly used as start station is', common_start_station)

    # TO DO: display most commonly used end station
    print('Most commonly used as end station is', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print()
    print('Most frequent combination of start station and end station is {}.'.format(freq_combination.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print()
    travel_sum = math.ceil(df['Trip Duration'].sum())
    sum_d = travel_sum // (24 * 3600)
    travel_sum = travel_sum % (24 * 3600)
    sum_h = travel_sum // 3600
    travel_sum %= 3600
    sum_m = travel_sum // 60
    travel_sum %= 60
    sum_s = travel_sum

    print('Total travel time is {} day(s), {} hour(s), {} minute(s), {} second(s).'.format(sum_d, sum_h, sum_m, sum_s))

    # TO DO: display mean travel time
    print()
    travel_mean = math.ceil(df['Trip Duration'].mean())
    mean_d = travel_mean // (24 * 3600)
    travel_mean = travel_mean % (24 * 3600)
    mean_h = travel_mean // 3600
    travel_mean %= 3600
    mean_m = travel_mean // 60
    travel_mean %= 60
    mean_s = travel_mean

    print('Mean travel time is {} hour(s), {} minute(s), {} second(s).'.format(mean_h, mean_m, mean_s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print()
    user_types = df['User Type'].value_counts()
    print('There are following types of users: \n{}'.format(user_types.to_string()))

    # TO DO: Display counts of gender
    print()
    if 'Gender' not in df:
        print('Unfortunately, there is no gender data for this city.')
    else:
        gender_type = df['Gender'].value_counts()
        print('There are following numbers of users\' gender: \n{} '.format(gender_type.to_string()))

    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    if 'Birth Year' not in df:
        print('Unfortunately, there is no year of birth data for this city.')
    else:
        mean_by = int(df['Birth Year'].mode()[0])
        min_by = int(df['Birth Year'].min())
        max_by = int(df['Birth Year'].max())


        print('The earliest year of birth is {}. \nThe most recent year of birth is {}. \nMost common year of birth is {}.'.format(min_by, max_by, mean_by))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Displays 5 rows of raw data."""

    i = 0
    # TO DO: convert the user input to lower case using lower() function
    raw = input("Do you want to have a look at some raw data? Yes/Y or No/N. ").lower()
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no' or raw == 'n':
            break
        elif raw == 'yes' or raw == 'y':
            print(df.iloc[i]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Do you want to have a look at some more of raw data? Yes/Y or No/N. ") # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'Yes/Y' or 'No/N'. ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)



        restart = input('\nWould you like to restart? Enter Yes/Y or No/N. ').lower()
        while restart not in ['yes', 'y', 'no', 'n']:
            print("\nYour input is invalid. Please enter only 'Yes/Y' or 'No/N'. ")
            restart = input('\nWould you like to restart? Enter Yes/Y or No/N. ').lower()
        if restart == 'no' or restart == 'n':
            break



if __name__ == "__main__":
	main()
