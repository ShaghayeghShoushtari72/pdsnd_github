import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        city = input("Enter city name (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please choose from chicago, new york city, washington.")
    
    while True:
        month = input("Enter month name or 'all': ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month name. Please enter a valid month or 'all'.")
    
    while True:
        day = input("Enter day of the week or 'all': ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid day of the week. Please enter a valid day or 'all'.")

    print('-'*40)
    return city, month, day

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no: ").lower()



def load_data(city, month, day):
    file_path = CITY_DATA.get(city)
    if file_path is None:
        print("Invalid city name. Please choose from chicago, new york city, washington.")
        return None

    df = pd.read_csv(file_path)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print("Most common month:", common_month)

    common_day = df['day_of_week'].mode()[0]
    print("Most common day of week:", common_day)

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most common start hour:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print("Most common start station:", common_start_station)

    common_end_station = df['End Station'].mode()[0]
    print("Most common end station:", common_end_station)

    df['Start_End_Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_start_end_combination = df['Start_End_Combination'].mode()[0]
    print("Most common start-end station combination:", common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types_counts = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types_counts)

    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:\n", gender_counts)
    else:
        print("Gender data not available.")

    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("Earliest birth year:", earliest_birth_year)
        print("Most recent birth year:", most_recent_birth_year)
        print("Most common birth year:", most_common_birth_year)
    else:
        print("Birth year data not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        if city == 'exit':
            break
        df = load_data(city, month, day)
        
        if df is not None:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            
            display_data(df)

            restart = input('\nWould you like to restart? Enter yes or exit.\n')
            if restart.lower() != 'yes':
                break

if __name__ == "__main__":
    main()