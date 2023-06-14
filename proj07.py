###########################################################

    #  Computer Project #07
    #
    #  Algorithm
    #           This program imports the csv file to be used, it also calls the operator function to import itemgetter. 
    #           The program also imports the datetime function from the datetime module
    #           The program reads data from multiple csv files 
    #           The program has 9 functions and 1 main function. 
    #           The docstrings for the various functions have been included in the functions. 
    #           The functions:
    #                          1. open_files()
    #                          2. read_files()
    #                          3. get_data_in_range()
    #                          4. get_min()
    #                          5. get_max()
    #                          6. get_average()
    #                          7. get_modes()
    #                          8. high_low_averages()
    #                          9. display_statistics()

    #           The main_function():
    #                  1. calls the open_file function to ask the user for a list of cities separated by commas and finds csv files with the cities' name. 
    #                  2. calls the read_file function to read the data and store it in a list of list of tuples.
    #                  3. A while loop to keep taking the option from the user until the option is 7.
    #                       a. if option is 1:
    #                                         i. prompts the user for a for a start and end dates to extract data within this range. 
    #                                         ii. prompts the user for a desired category 
    #                                         iii. call the get_max function and pass the filtered data, cities, and the column index of the category as arguments. 
    #                                         iv. Display the maximum of that category for each city 
    #                       b.if option is 2:
    #        
    #                                       i. prompts the user for a for a start and end dates to extract data within this range. 
    #                                       ii. prompts the user for a desired category 
    #                                       iii. call the get_min function and pass the filtered data, cities, and the column index of the category as arguments. 
    #                                       iv. Display the minimum of that category for each city  

    #                       c. if option is 3:
    #                                          
    #                                      i. prompts the user for a for a start and end dates to extract data within this range. 
    #                                      ii. prompts the user for a desired category 
    #                                      iii. call the get_average function and pass the filtered data, cities, and the column index of the category as arguments. 
    #                                      iv. Display the average of that category for each city

    #                       d. if option is 4:
    #                                       i. prompts the user for a for a start and end dates to extract data within this range. 
    #                                      ii. prompts the user for a desired category 
    #                                      iii. call the get_modes function and pass the filtered data, cities, and the column index of the category as arguments. 
    #                                      iv. Display the most common repeated values (Modes) for that category for each city

    #                       e. if option is 5:
    #                                        i. prompts the user for a for a start and end dates to extract data within this range. 
    #                                      ii. prompts the user for a desired category 
    #                                      iii. call the display_statistics function and pass the filtered data, cities, and the column index of the category as arguments. 
    #                                      iv. Display the summary statistics for each city: minimum, maximum, average, and list of modes for the category. 
    #
    #
    #                       f. if option is 6:
    #                                       i. prompts the user for a for a start and end dates to extract data within this range. 
    #                                      ii. prompts the user for a desired categories separated by commas
    #                                      iii. call the high_low__averages function and pass the filtered data, cities, and the desired categories list in to it.  
    #                                      iv. For invalid categories, display an error message 
    #                                      v. Display the cities with the highest and lowest average across all cities for each category. 
    #
    #                       g. if option is 7:
    #                                       i. print a goodbye message 
    #                                       ii. Quit the program 
    #
###########################################################################################################################################################################################################

import csv
from datetime import datetime
from operator import itemgetter

COLUMNS = ["date",  "average temp", "high temp", "low temp", "precipitation", \
           "snow", "snow depth"]

TOL = 0.02

BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'    


MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''
        
def open_files():
    """
    This function prompts the user to enter a series of cities separated by comma and returns a list of
    cities and a list of file pointers that correspond to that list of cities. 
    Prints error message if city is not found, do not include its file pointer.

    Returns:
    - A tuple containing two lists:
        - A list of valid city names (without the .csv extension)
        - A list of file pointers for the corresponding valid city names
    """
    cities = input("Enter cities names: ").split(",")
    cities_fp = []
    valid_cities = []

    #iterate through every city in the cities list and append the csv extension to it. 
    #Check if there is a file with such extension, if not print file not found. 
    #if it is found, returns a list of file pointers.
    for city in cities:
        filename = city.strip() + ".csv"
        try:
            fp = open(filename, "r", encoding="utf-8")
            cities_fp.append(fp)
            valid_cities.append(city.strip())
        except FileNotFoundError:
            print("\nError: File {} is not found".format(filename))

    return valid_cities, cities_fp

def read_files(cities_fp):
    """
    Reads in data from csv files and returns a list of lists of tuples.
    Ignore the headers in each file (skip the first two lines).
    Replace missing values with None. Each list has the same length of 6.
    Each tuple has the following format: (Date, TAVG, TMAX, TMIN, PRCP, SNOW, SNWD)

    set up helper function called process line to process data from a single line
    in a csv file and returns a tuple with the values.

    :param cities_fp: a list of file pointers
    :return: a list of lists of tuples
    """
    def process_line(line):
        # Process a line from a csv file and return a tuple
        values = line.strip().split(",")
        if len(values) != 7:
            return None
        # Convert temperature values to floating-point values
        TAVG = float(values[1]) if values[1] else None
        TMAX = float(values[2]) if values[2] else None
        TMIN = float(values[3]) if values[3] else None
        PRCP = float(values[4]) if values[4] else None
        SNOW = float(values[5]) if values[5] else None
        SNWD = float(values[6]) if values[6] else None
        return (values[0], TAVG, TMAX, TMIN, PRCP, SNOW, SNWD) 

    result = []
    for fp in cities_fp:
        fp.readline()  # skip first two lines
        fp.readline()
        inner_list = []
        for line in fp:
            processed = process_line(line)
            if processed:
                inner_list.append(processed)       #append a list of values from the helper function 
        result.append(inner_list)
        fp.close()                                 #close the file after reading 

    return result


def get_data_in_range(data, start_date_str, end_date_str):
    '''Filters the data based on the given dates. it uses the datetime function in 
    python for its operation. Compares the dates at index 0 of each list of tuple
    to the given start and end dates and outputs a list of tuples containing dates 
    in the specifies range. 
    
    parameters: list of tuples,tuple,tuple,tuple,int
    Returns: list of tuples 
    '''
    
    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start_date_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_date_str, "%m/%d/%Y").date()
    
    # Filter the data based on the date range
    filtered_data = []
    for sublist in data:
        filtered_sublist = []
        for tup in sublist:
            date = datetime.strptime(tup[0], "%m/%d/%Y").date()     #check to see if the given date from the data is in between the start and end dates given,
            if start_date <= date <= end_date:
                filtered_sublist.append(tup)                        #append all data in this range
        if filtered_sublist:
            filtered_data.append(filtered_sublist)                  #append all the tuples into a list of tuples
    
    return filtered_data



def get_min(col, data, cities):
    """
    Returns a list of tuples containing the name of each city in `cities` and the minimum value
    in the `col` index of each tuple in the corresponding list of tuples in `data`.
    
    Args:
        col (int): The index of the column to search for minimum value.
        data (List[List[Tuple]]): A list of lists of tuples representing weather data for each city.
        cities (List[str]): A list of city names corresponding to each list of tuples in `data`.
    
    Returns:
        List[Tuple[str, float]]: A list of tuples containing the name of each city and the minimum value
        in the `col` index of each tuple in the corresponding list of tuples in `data`.
    """
    # Create an empty list to hold the result
    min_values = []
    
    # Loop through each list of tuples in `data`
    for i, city_data in enumerate(data):
        
        # Set the minimum value to a very large number
        min_value = float('inf')
        
        # Loop through each tuple in the list of tuples for this city
        for tup in city_data:
            
            # Check if the value at the given column index is not None and less than the current minimum value
            if tup[col] is not None and tup[col] < min_value:
                
                # Update the minimum value
                min_value = tup[col]
        
        # Append a tuple containing the name of the city and the minimum value to the result list
        min_values.append((cities[i], min_value))
    
    # Return the list of tuples containing the name of each city and the corresponding minimum value
    return min_values


def get_max(col, data, cities):
    """
    Finds the maximum value of the corresponding column col for each city in cities
    and returns a list of tuples of the following form: [(city,max_value),…].

    Args:
        col (int): The index of the column to search for the max value 
        data (list[list[tuples]]): A list of list of tuples representing weather data for each city
        cities (list[str]): A list of city names corresponding to each list of data in 'data'

    Returns:
        List([Tuple[str, float]]): A list of tuples containing the name of each city and the maximum value 
        in the "col" index of each tuple in the corresponding list of tuples in 'data'. 
    """
    #create an empty list to hold the max_values. 
    max_values = []
    #loop through each list of tuples in data
    for i, city_data in enumerate(data):
        max_value = float('-inf')               #set the max_value to a very small number
        for tup in city_data:                   #loop through each tuple in the list of tuples for a particular city
            if tup[col] is not None and tup[col] > max_value:
                max_value = tup[col]
        max_values.append((cities[i], max_value))        #append the city_name and the max_value  

    return max_values


def get_average(col, data, cities):
    """
    This function returns a list of list of tuples. 
    Args:
        col (int): The index of the column to search for the max value 
        data (list[list[tuples]]): A list of list of tuples representing weather data for each city
        cities (list[str]): A list of city names corresponding to each list of data in 'data'
    Returns:
        List([Tuple[str, float]]): A list of tuples containing the name of each city and the maximum value 
        in the "col" index of each tuple in the corresponding list of tuples in 'data'.

    """
    #create an empty list to hold the avg_values. 
    avg_values = []
    for i, city_data in enumerate(data):
        col_data = [tup[col] for tup in city_data if tup[col] is not None]  #list comprehension to append all the values in the column that are not empty 
        avg_value = round(sum(col_data) / len(col_data), 2) if len(col_data) > 0 else None   #calculate the average value and round to two decimal places
        avg_values.append((cities[i], avg_value))                                            #append the city_name and the average value to the avg_values list 

    return avg_values 

def get_modes(col, data, cities):
    """
    Computes the mode(s) of the given column for each city.

    Parameters:
    col (int): Index of the column to compute modes for.
    data (list of list of tuples): List of lists of tuples representing the data for each city.
    cities (list of strings): List of city names to compute modes for.

    Returns:
    A list of tuples, where each tuple contains the name of a city, the mode(s) of the given column for that city,
    and the number of non-None values in that column for that city.
    """
    modes_list = []
    for i, city_data in enumerate(data):
        city = cities[i]
        # get the column of interest from the city data and remove any None values
        column = [row[col] for row in city_data if row[col] is not None]
        column.sort()  # sort the column in ascending order
        
        modes = []
        max_count = 0
        j = 0
        while j < len(column):
            count = 1
            # check if the next value is within 2% of the current value
            while j + count < len(column) and column[j] != 0 and abs((column[j + count] - column[j]) / column[j]) <= TOL:
                count += 1
            # if there are multiple values within 2% of each other, they are all considered modes
            if count > 1:
                if count > max_count:
                    max_count = count
                    modes = [column[j]]
                    
                elif count == max_count:
                    modes.append(column[j])
                    
                j += count
            else:
                j += 1
        
        if len(modes) == 0:
            max_count = 1 
            modes_list.append((city, modes, max_count))
        else:
            modes_list.append((city, modes, max_count))  # add the city's modes and number of non-None values to the list

    return modes_list

          

def high_low_averages(data, cities, categories):
    """
    Return a list of tuples, with each tuple containing the name of the city with the lowest
    average value and the name of the city with the highest average value for each category in categories.

    Parameters:
            List of list of tuples
            lIst of strings 
            list of strings 

    Returns:
            list of list of tuples 

    """

    # Create an empty list to store the results
    results = []

    # Loop over each category
    for category in categories:
        # Check if the category is in the COLUMNS list
        if category not in COLUMNS:
            results.append(None)
            continue

        # Get the column index for the current category
        col_index = COLUMNS.index(category)

        # Get the average values for the current category for each city
        averages = get_average(col_index, data, cities)

        # Sort the cities by their average values for the current category
        sorted_averages = sorted(averages, key=itemgetter(1))

        # Get the city with the lowest average for the current category
        lowest_city, lowest_average = sorted_averages[0]

        # Get the city with the highest average for the current category
        highest_city, highest_average = sorted_averages[-1]

        # If there is a tie for the highest or lowest average values, use the first city that appears in the original list
        for city, average in sorted_averages:
            if average == lowest_average:
                lowest_city = city
                break
        for city, average in sorted_averages:
            if average == highest_average:
                highest_city = city
                break

        # Add a tuple with the lowest and highest cities and their average values for the current category
        results.append([(lowest_city, lowest_average), (highest_city, highest_average)])

    # Return the results
    return results


def display_statistics(col, data, cities):
    """
    Displays summary statistics for each city, including min, max, average, and mode.

    Parameters:
    col (int): Index of the column to compute statistics for.
    data (list of list of tuples): List of lists of tuples representing the data for each city.
    cities (list of strings): List of city names to display statistics for.

    Returns:
    None
    """


    Min_value = get_min(col, data, cities)          #Get the minimum values from the given data and the cities and column index
    Max_value = get_max(col, data, cities)          #Get the Maximum values from the given data and the ciies and column index
    Avg_value = get_average(col, data, cities)      #Get the Average values from the given data and the cities and column index
    Modes = get_modes(col, data, cities)            #Get the Modes from column index, the given data and the cities 

    for i in range(len(Max_value)):
        print("\t{}: ".format(cities[i]))
        print("\tMin: {:.2f} Max: {:.2f} Avg: {:.2f}".format(Min_value[i][1], Max_value[i][1], Avg_value[i][1]))

        actual_modes = Modes[i][1]

        if len(actual_modes) == 0:
            print("\tNo modes.")

        else:
            added_modes = ", ".join([str(mode) for mode in actual_modes])
            print("\tMost common repeated values ({:d} occurrences): {:s}\n".format(Modes[i][2],added_modes))


            
def main():
    print(BANNER)
    cities, fp = open_files()
    data = read_files(fp)
    
    
    while True:

        option = int(input(MENU))

        #if option is 7 print a goodbye message and quit the program 
        if option == 7:
            print("\nThank you using this program!")
            break 

        if option == 1:
            
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")    #ask user for start date
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")       #ask user for end date
            category = input("\nEnter desired category: ").lower()               #ask user for category
            filtered_data = get_data_in_range(data, start, end)                  #filter the data according to the start and end dates 

            while category not in COLUMNS:                                       #keep prompting the user for a category if it is not in the columns
                print( "\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()


            else: 
                print("\n\t{}: ".format(category))                               #print the category 
                col = COLUMNS.index(category)
                max_values = get_max(col, filtered_data,cities)                  #get the maximum values from the filtered data 


                for i in range(len(max_values)):
                    print("\tMax for {:s}: {:.2f}".format(max_values[i][0],max_values[i][1]))    #display the maximum value 


        elif option == 2:
            
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ") 
            category = input("\nEnter desired category: ").lower()
            filtered_data = get_data_in_range(data, start, end)

            while category not in COLUMNS:
                print( "\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()

            else: 
                print("\n\t{}: ".format(category))                                              #print the category
                col = COLUMNS.index(category)
                min_values = get_min(col, filtered_data,cities)                                 #get the minimum value from the filtered data

                for i in range(len(min_values)):
                    print("\tMin for {:s}: {:.2f}".format(min_values[i][0],min_values[i][1]))   #display the minimum value 

        
        elif option == 3:
            
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ") 
            category = input("\nEnter desired category: ").lower()
            filtered_data = get_data_in_range(data, start, end)

            while category not in COLUMNS:
                print( "\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()

            else: 
                print("\n\t{}: ".format(category))                                             #print the category 
                col = COLUMNS.index(category)
                avg_values = get_average(col, filtered_data,cities)                            #get the average values from the filtered data 

                for i in range(len(avg_values)):
                    print("\tAverage for {:s}: {:.2f}".format(avg_values[i][0],avg_values[i][1]))    #display the average value 

        elif option == 4:
            
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ") 
            category = input("\nEnter desired category: ").lower()
            filtered_data = get_data_in_range(data, start, end)

            while category not in COLUMNS:
                print( "\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()

            else: 
                print("\n\t{}: ".format(category))                 #print category
                col = COLUMNS.index(category)
                Modes = get_modes(col, filtered_data,cities)       #get the modes from the filtered data 

                for i in range(len(Modes)):
                     
                    actual_modes = Modes[i][1]                     #Get all the modes from the list of tuples           
                    city_name = Modes[i][0]                        #get the name of the city from the list of tuples 

                    if len(actual_modes) == 0:                     #if there are no modes, print No modes 
                        print("\tNo modes.")

                    else:
                        added_modes = ", ".join([str(mode) for mode in actual_modes])       #use list comprehension to join the modes as a string 
                        print("\tMost common repeated values for {:s} ({:d} occurrences): {:s}\n".format(city_name,Modes[i][2],added_modes))  #display the modes 

        elif option == 5:
            
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ") 
            category = input("\nEnter desired category: ").lower()
            filtered_data = get_data_in_range(data, start, end)

            while category not in COLUMNS:
                print( "\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()

            else: 
                print("\n\t{}: ".format(category))            #print the category 
                col = COLUMNS.index(category)
                display_statistics(col, filtered_data,cities)       #display the statistics from each city 
        
        elif option == 6:

            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            categories = input("\nEnter desired categories seperated by comma: ").lower().split(',')
            filtered_data = get_data_in_range(data, start, end)

            print("\nHigh and low averages for each category across all data.")
            
            
            averages = high_low_averages(filtered_data,cities,categories)
            for i in range(len(averages)):
                try:
                    low_city_name = averages[i][0][0]               #set name of city with low average
                    low_avg = averages[i][0][1]                     #get the low average value
                    high_city_name = averages[i][1][0]              #set name of city with high average
                    high_avg = averages[i][1][1]                    #get the high average value 
                    print("\n\t{}: ".format(categories[i]))
                    print("\tLowest Average: {:s} = {:.2f} Highest Average: {:s} = {:.2f}".format(low_city_name,low_avg,high_city_name,high_avg)) #display the high_low_averages 

                except:
                    print("\n\t{} category is not found.".format(categories[i]))


#DO NOT CHANGE THE FOLLOWING TWO LINES OR ADD TO THEM
#ALL USER INTERACTIONS SHOULD BE IMPLEMENTED IN THE MAIN FUNCTION
if __name__ == "__main__":
    main()
            
