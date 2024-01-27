# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mobile_app_data_analysis.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: andrefrancisco <andrefrancisco@student.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/26 18:14:32 by abaiao-r          #+#    #+#              #
#    Updated: 2024/01/27 21:07:31 by andrefranci      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# csv is a built-in module in python that allows us to read and write to csv 
# files
import csv

# explore_data() function: allows us to explore the rows and columns of a 
# dataset
# dataset: list of lists
# start and end: integers that slice the dataset
# rows_and_columns: boolean parameter with False as default argument
# return: nothing, just prints the number of rows and columns and slices the 
# dataset
def explore_data(dataset, start, end, rows_and_columns = False):
    dataset_slice = dataset[start:end];
    for i in dataset_slice:
        print(i);
        print("\n");
        
    if rows_and_columns:
        print("Number of rows: ", len(dataset));
        print("Number of columns: ", len(dataset[0]));
  
# open_csv() function: allows us to open a csv file and transform it into a list 
# of lists
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
    data_header = data[0];
    data = data[1:];
    csv_file.close();
    return (data, data_header);

# print_separator() function: prints a separator
# return: nothing, just prints a separator
def print_separator():
    print("\n");
    print("----------------------------------------\n");
    print("\n");

# print the headers and datasets() function: prints the headers and datasets
# header: list of strings
# dataset: list of lists
# dataset_name: string that represents the name of the dataset (optional)
# return: nothing, just prints the headers and datasets
def print_headers_and_datasets(header, dataset, dataset_name = None):
    if (dataset_name != None):
        print(dataset_name + ": \n");
    
    if (header):
        print(header);
        print("\n");
        
    if (dataset):
        explore_data(dataset, 0, 3, True);
        print_separator();

# File paths for the datasets
google_play_store_file = "googleplaystore.csv";
apple_store_file = "AppleStore.csv";

# initialize the datasets and headers
google_play_store_data = None;
google_play_store_header = None;
apple_store_data = None;
apple_store_header = None;

# Open the datasets
google_play_store_data, google_play_store_header = open_csv(google_play_store_file);
apple_store_data, apple_store_header = open_csv(apple_store_file);

# print the headers and datasets
#print_headers_and_datasets(google_play_store_header, google_play_store_data, "Google Play Store");
#print_headers_and_datasets(apple_store_header, apple_store_data, "Apple Store");


# Data cleaning

# is_free_app() function: checks if the app is free
# row: list of strings
# header: list of strings
# index: integer that represents the index of the list that we want to check
# return: boolean that represents if the app is free or not
def is_free_app(row, header, index, printing_non_free_apps=False):
    #lowercase the header
    header_copy = [i.lower() for i in header];
    #look for the index of the price in header_copy ("price")
    index_price = header_copy.index("price");
    #lowercase row
    row_copy = [i.lower() for i in row];
    #check if the price is 0.0 or "0" or "free" in row_copy
    if (row_copy[index_price] == "0" or row_copy[index_price] == "0.0" or row_copy[index_price] == "free"):
        if (printing_non_free_apps == True):
            print(f"Not free app at index{index}: {row}\n");
        return (True);
    return (False);

# match_number_of_columns() function: checks if the row has the correct number
# of columns by comparing the length of the row with the length of the header
# row: list of strings
# header_length: integer that represents the length of the header
# index: integer that represents the index of the list that we want to check
# return: boolean that represents if the row has the correct number of columns
def match_number_of_columns(row, header_length, index, printing_wrong_number_of_columns=False):
    if (len(row) != header_length):
        if (printing_wrong_number_of_columns == True):
            print(f"Wrong number of columns at index {index}: {row}\n");
        return (False);
    return (True);

# is_english() function: checks if a the all row is in english characters
# row: list of strings
# printing_non_english: boolean that represents if we want to print the non
# english rows
# return: boolean that represents if the row is in english or not
def is_english(row, printing_non_english=False):
    for i in row:
        for j in i:
            if (ord(j) > 127):
                if (printing_non_english == True):
                    print(f"Not English at index {row.index(i)}: {i}\n");
                return (False);
    return (True);

# has_duplicates() function: checks if the row has duplicates
# cleaned_dataset: list of lists
# row: list of strings
# header: list of strings
# index: integer that represents the index of the list that we want to check
# printing_duplicates: boolean that represents if we want to print the duplicates
# return: boolean that represents if the row has duplicates or not
def has_duplicates(cleaned_dataset, row, header, index, printing_duplicates=False):
    #look for the index of the app name in header ("App" or "track_name")
    try:
        index_app_name = header.index("App");
    except ValueError:
        try:
            index_app_name = header.index("track_name");
        except ValueError:
            pass;
    #check if the app name is in cleaned_dataset
    for i in cleaned_dataset:
        if (row[index_app_name] == i[index_app_name]):
            if (printing_duplicates == True):
                print(f"Duplicate at index {index}: {row}\n");
            # check which one has the highest number of reviews
            try:    
                index_reviews = header.index("Reviews");
                if (int(row[index_reviews]) > int(i[index_reviews])):
                    # remove the one with the lowest number of reviews and append the new one
                    del cleaned_dataset[cleaned_dataset.index(i)];
                    cleaned_dataset.append(row);
                    return (True);
            except ValueError:
                pass;
            try:
                index_reviews = header.index("rating_count_tot");
                if (int(row[index_reviews]) > int(i[index_reviews])):
                    # remove the one with the lowest number of reviews and append the new one
                    del cleaned_dataset[cleaned_dataset.index(i)];
                    cleaned_dataset.append(row);
                    return (True);
            except ValueError:
                pass;
            return (True);
    return (False);


# check_row_and_delete() function: checks if the row has duplicates, if the app
# is free, if the row has the correct number of columns and if the row is in
# english. If it doesn't, it deletes the row.
# dataset: list of lists
# header: list of strings
# name_of_dataset: string that represents the name of the dataset (optional)
# return: the cleaned dataset as a list of lists
def check_row_and_delete(dataset, header, name_of_dataset=None):
    if (dataset == None):
        print("Error: no dataset provided\n");
        return (None);
    
    if (header == None):
        print("Error: no header provided\n");
        return (None);
    
    header_length = len(header);
    dataset_length = len(dataset);
    cleaned_dataset = [];
    duplicates = 0;
    
    for i in dataset:
        # check duplicates
        if (has_duplicates(cleaned_dataset, dataset[dataset.index(i)], header, dataset.index(i), False)):
            #print(f"Duplicate in dataset at index {dataset.index(i)}: {i}");
            #print_separator();
            duplicates += 1;
            continue;
        if (not is_english(dataset[dataset.index(i)], False)):
            #print(f"Non-English in dataset at index {dataset.index(i)}: {i}");
            #print_separator();
            continue;
        if (not match_number_of_columns(dataset[dataset.index(i)], header_length, dataset.index(i), False)):
            #print(f"Wrong number of columns in dataset at index {dataset.index(i)}: {i}");
            #print_separator();
            continue;
        if (not is_free_app(dataset[dataset.index(i)], header, dataset.index(i), False)):
            #print(f"Not free app in dataset at index {dataset.index(i)}: {i}");
            #print_separator();
            continue;
        cleaned_dataset.append(i);
    #print nbr of rows before and after
    cleaned_dataset_length = len(cleaned_dataset);
    print(f"Number of rows before of {name_of_dataset}: {dataset_length}");
    print(f"Number of rows after of {name_of_dataset}: {cleaned_dataset_length}");
    print(f"Number of duplicates of {name_of_dataset}: " + str(duplicates));
    return (cleaned_dataset);

# clean the datasets
google_play_store_data_cleaned = check_row_and_delete(google_play_store_data, google_play_store_header, "Google Play Store");
apple_store_data_cleaned = check_row_and_delete(apple_store_data, apple_store_header, "Apple Store");


# print the headers and datasets
print_headers_and_datasets(google_play_store_header, google_play_store_data_cleaned, "Google Play Store");
print_headers_and_datasets(apple_store_header, apple_store_data_cleaned, "Apple Store");

        
                    