# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mobile_app_data_analysis.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/26 18:14:32 by abaiao-r          #+#    #+#              #
#    Updated: 2024/01/26 18:58:24 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# csv is a built-in module in python that allows us to read and write to csv files
import csv

# explore_data() function: allows us to explore the rows and columns of a dataset
# dataset: list of lists
# start and end: integers that slice the dataset
# rows_and_columns: boolean parameter with False as default argument
# return: nothing, just prints the number of rows and columns and slices the dataset
def explore_data(dataset, start, end, rows_and_columns = False):
    dataset_slice = dataset[start:end];
    for i in dataset_slice:
        print(i);
        print("\n");
        
    if rows_and_columns:
        print("Number of rows: ", len(dataset));
        print("Number of columns: ", len(dataset[0]));
  
# open_csv() function: allows us to open a csv file and transform it into a list of lists
# file_name: string that contains the name of the file, including the extension
# return: the dataset as a list of lists      
def open_csv(file_name):
    if (file_name == None):
        print("Error: no file name provided\n");
        return (None);
    
    try:
        csv_file = open(file_name, encoding="utf-8");
    except FileNotFoundError:
        print(f"Error: {file_name} not found");
        return (None);
    except Exception as e:
        print(f"Error: {e}");
        return (None);
    
    csv_reader = csv.reader(csv_file);
    data = list(csv_reader);
    csv_file.close();
    return (data);

# print_column_names() function: prints the column names of a dataset
# dataset: list of lists
# return: nothing, just prints the column names of the dataset
def print_column_names(dataset):
    if (dataset == None):
        print("Error: no dataset provided\n");
        return;
    
    print("Column names: \n");
    for i in dataset[0]:
        print(i);
        print("\n");

# print_separator() function: prints a separator
# return: nothing, just prints a separator
def print_separator():
    print("\n");
    print("----------------------------------------\n");
    print("\n");

# File paths for the datasets
google_play_store_file = "googleplaystore.csv";
apple_store_file = "AppleStore.csv";

# Open the datasets
google_play_store_data = open_csv(google_play_store_file);
apple_store_data = open_csv(apple_store_file);

# Print the column names of the datasets
if (google_play_store_data):
    print_column_names(google_play_store_data);
    print_separator();
    
if (apple_store_data):
    print_column_names(apple_store_data);
    print_separator();

# Explore the datasets by printing the first few rows to verify everything works if the datasets are loaded correctly
if (google_play_store_data):
    print("Google Play Store Data: \n");
    explore_data(google_play_store_data, 0, 5, True);
    print_separator();
    
if (apple_store_data):
    print("Apple Store Data: \n");
    explore_data(apple_store_data, 0, 5, True);
    print_separator();
    
    
    
