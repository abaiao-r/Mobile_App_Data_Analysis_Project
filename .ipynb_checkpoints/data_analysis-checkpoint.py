# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_analysis.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/30 15:28:38 by abaiao-r          #+#    #+#              #
#    Updated: 2024/01/30 15:35:13 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# freq_table() function: generates a frequency table for any column we want in
# our dataset
# dataset: list of lists
# index: integer that represents the index of the list that we want to check
# return: a dictionary that represents the frequency table
def freq_table(dataset, index):
    freq_table = {};
    total = 0;
    for i in dataset:
        total += 1;
        if (i[index] in freq_table):
            freq_table[i[index]] += 1;
        else:
            freq_table[i[index]] = 1;
    for i in freq_table:
        freq_table[i] = (freq_table[i] / total) * 100;
    return (freq_table);



#Another function we can use to display the percentages in a descending order
# is display_table() function:
# dataset: list of lists
# index: integer that represents the index of the list that we want to check
# return: nothing, just prints the frequency table in a descending order
def display_table(dataset, index):
    table = freq_table(dataset, index);
    table_display = [];
    for i in table:
        key_val_as_tuple = (table[i], i);
        table_display.append(key_val_as_tuple);
    table_sorted = sorted(table_display, reverse=True);
    for i in table_sorted:
        print(i[1], ":", i[0]);
        
# avg_nbr_of_user_ratings_per_genre() function: calculates the average number of
# user ratings per genre
# dataset: list of lists
# header: list of strings
# index: integer that represents the index of the list that we want to check
# return: nothing, just prints the average number of user ratings per genre
def avg_nbr_of_user_ratings_per_genre(dataset, header, index):
    genre_freq_table = freq_table(dataset, index);
    avg_nbr_of_user_ratings_per_genre = {};
    for i in genre_freq_table:
        total = 0;
        len_genre = 0;
        for j in dataset:
            if (j[index] == i):
                total += float(j[header.index("rating_count_tot")]);
                len_genre += 1;
        avg_nbr_of_user_ratings_per_genre[i] = total / len_genre;
    return (avg_nbr_of_user_ratings_per_genre);



# avg_installs_per_category() function: calculates the average number of installs
# per category
# dataset: list of lists
# index_category: integer that represents the index of the list that we want to check
# index_installs: integer that represents the index of the list that we want to check
# return: nothing, just prints the average number of installs per category
def avg_installs_per_category(dataset, index_category, index_installs):
    # Create a frequency table for the Category column
    category_freq_table = freq_table(dataset, index_category)
    category_avg_nbr_installs = {}

    # For each category...
    for category in category_freq_table:
        total = 0  # Sum of installs specific to each genre
        len_category = 0  # Number of apps specific to each genre

        # For each app...
        for app in dataset:
            category_app = app[index_category]
            
            # If the app's category matches the current category...
            if category_app == category:
                n_installs = app[index_installs]
                n_installs = n_installs.replace(',', '')
                n_installs = n_installs.replace('+', '')
                total += float(n_installs)
                len_category += 1

        # Compute the average number of installs
        avg_n_installs = total / len_category
        category_avg_nbr_installs[category] = avg_n_installs;
    return (category_avg_nbr_installs);

def split_by_column_value(data, column_index):
    splitted_data = {};

    for row in data:
        column_value = row[column_index];

        if (column_value in splitted_data):
            splitted_data[column_value].append(row);
        else:
            splitted_data[column_value] = [row];
    return (splitted_data);

def calculate_total_per_category(data_split_by_category, index):
    total_per_category = {}
    for category in data_split_by_category:
        total = 0
        for item in data_split_by_category[category]:
            total += float(item[index].replace("+", "").replace(",", ""))
        total_per_category[category] = total
    return total_per_category

def calculate_percentage_of_value_per_category(data_split_by_category, index_value):
    total_per_category = calculate_total_per_category(data_split_by_category, index_value)
    percentage_of_value_per_category = {}
    for category in data_split_by_category:
        percentage_of_value_per_category[category] = []
        for item in data_split_by_category[category]:
            percentage = round(float(item[index_value].replace("+", "").replace(",", "")) / total_per_category[category] * 100, 2)
            percentage_of_value_per_category[category].append([item[0], item[index_value], percentage])
    return percentage_of_value_per_category

def add_percentage_column(data_split_by_category, index_value):
    total_per_category = calculate_total_per_category(data_split_by_category, index_value)
    data_with_percentage = {}
    for category in data_split_by_category:
        data_with_percentage[category] = []
        for item in data_split_by_category[category]:
            percentage = round(float(item[index_value].replace("+", "").replace(",", "")) / total_per_category[category] * 100, 2)
            data_with_percentage[category].append(item + [percentage])
    return data_with_percentage

