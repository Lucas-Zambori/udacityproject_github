import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    accepted_cities = ["chicago", "new york city", "washington"]

    while True:
        city = input("Which city should we analyze? (Pick one of the following: Chicago, New York City, Washington) : ").strip().lower()
        if city in accepted_cities:
            print(f"Perfect! Let's analyze: {city.title()}")
            break
        else:
            print("Sorry we don't have data on that city, please select one of the cities listed in the previous prompt.")

    # Get user input for month (all, january, february, ... , june)
    accepted_months = ["all", "january", "february", "march", "april", "may", "june"]

    while True:
        month = input("Which month should we analyze? (Pick one of the following: All, January, February, March, April, May, June) : ").strip().lower()
        if month in accepted_months:
            print(f"Perfect! Let's analyze: {month.title()}")
            break
        else:
            print("Sorry we don't have data on that month, please select one of the months listed in the previous prompt.")

    # Get user input for day (all, monday, tuesday, ... sunday)
    accepted_days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    while True:
        day = input("Which day should we analyze? (Pick one of the following: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) : ").strip().lower()
        if day in accepted_days:
            print(f"Perfect! Let's analyze: {day.title()}")
            break
        else:
            print("Sorry, we don't have data to support that entry. Please select one of the options listed.")

    print('-' * 40)
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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Displays the most common month
    mode_month = df['month'].mode()[0]
    print(f"The most popular month is: {mode_month.title()}")

    # Displays the most common day of week
    mode_day = df['day_of_week'].mode()[0]
    print(f"The most popular day of the week is: {mode_day.title()}")

    # Displays the most common start hour
    mode_hour = df['hour'].mode()[0]
    print(f"The most popular start hour is: {mode_hour}:00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Displays most commonly used start station
    start_station_counts = df['Start Station'].value_counts()
    popular_start_station = start_station_counts.idxmax()
    start_station_count = start_station_counts.max()
    start_station_pct = (start_station_count / len(df)) * 100

    print(f"Most popular start station: {popular_start_station}")
    print(f"  Count: {start_station_count} ({start_station_pct:.2f}%)")
    print('-' * 40)

    # Display most commonly used end station
    end_station_counts = df['End Station'].value_counts()
    popular_end_station = end_station_counts.idxmax()
    end_station_count = end_station_counts.max()
    end_station_pct = (end_station_count / len(df)) * 100

    print(f"Most popular end station: {popular_end_station}")
    print(f"  Count: {end_station_count} ({end_station_pct:.2f}%)")
    print('-' * 40)

    # Display most frequent combination of start station and end station trip
    df['Start-End Combo'] = df['Start Station'] + " → " + df['End Station']
    combo_counts = df['Start-End Combo'].value_counts()
    popular_trip = combo_counts.idxmax()
    trip_count = combo_counts.max()
    trip_pct = (trip_count / len(df)) * 100

    print(f"Most popular trip (Start → End): {popular_trip}")
    print(f"  Count: {trip_count} ({trip_pct:.2f}%)")
    print('-' * 40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # Display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print(f"Average travel time: {average_travel_time:.2f} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_types_counts)
    print('-' * 40)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:")
        print(gender_counts)
    else:
        print("Sorry, gender data not available.")
    print('-' * 40)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])

        print(f"Earliest birth year: {earliest_year}")
        print(f"Most recent birth year: {most_recent_year}")
        print(f"Most common birth year: {most_common_year}")
    else:
        print("Sorry, birth year data not available.")
    print('-' * 40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    """Displays 5 lines of raw data if user selects yes."""
    row_index = 0
    step = 5
    total_rows = len(df)
    first_prompt = True

    while row_index < total_rows:
        if first_prompt:
            show_data = input("\nWould you like to see the first 5 lines of raw data? (Enter yes or no) ").strip().lower()
            first_prompt = False
        else:
            show_data = input("\nWould you like to see 5 more lines of raw data? (Enter yes or no) ").strip().lower()

        if show_data == 'yes':
            print(df.iloc[row_index:row_index + step])
            row_index += step
        elif show_data == 'no':
            print("Awesome, you've reached the end of the program!")
            break
        else:
            print("Sorry, that input wasn't valid (Please enter yes or no)")

    if row_index >= total_rows:
        print("You've reached the end of the raw data.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)

        restart = input('\nWould you like to restart? (Enter yes or no)\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
