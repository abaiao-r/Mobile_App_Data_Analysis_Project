# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mobile_app_data_analysis.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/26 18:14:32 by abaiao-r          #+#    #+#              #
#    Updated: 2024/01/30 15:35:28 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from data_extraction import *
from data_cleaninig import *
from data_analysis import *

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
print_headers_and_datasets(google_play_store_header, google_play_store_data, "Google Play Store");
print_headers_and_datasets(apple_store_header, apple_store_data, "Apple Store");


# Data cleaning

# clean the datasets
google_play_store_data_cleaned = check_row_and_delete(google_play_store_data, google_play_store_header, "Google Play Store");
apple_store_data_cleaned = check_row_and_delete(apple_store_data, apple_store_header, "Apple Store");


# print the headers and datasets
print_headers_and_datasets(google_play_store_header, google_play_store_data_cleaned, "Google Play Store");
print_headers_and_datasets(apple_store_header, apple_store_data_cleaned, "Apple Store");

# Data analysis

# We'll build two functions we can use to analyze the frequency tables:

# print the frequency tables of the genres and prime genres of the cleaned 
# datasets
print("Google Play Store - Genres: \n");
# look for the index of the genres in google_play_store_header ("Genres" or  
# "prime_genre" and "Category")
index_genres = google_play_store_header.index("Genres");
index_prime_genre = apple_store_header.index("prime_genre");
index_category = google_play_store_header.index("Category");
index_installs = google_play_store_header.index("Installs");
index_rating_count_tot = apple_store_header.index("rating_count_tot");

# display the frequency tables of the genres and prime genres of the cleaned 
# datasets
print("Google Play Store - Genres: \n");
display_table(google_play_store_data_cleaned, index_genres);
print("\n");
display_table(google_play_store_data_cleaned, index_category);
print("\n");
print("Apple Store - Prime Genres: \n");
display_table(apple_store_data_cleaned, index_prime_genre);     


# print the average number of user ratings per genre
print("\n");
print("Average number of user ratings per genre in AppStore: \n");
apple_store_data_avg_nbr_rating_per_genre = sorted(avg_nbr_of_user_ratings_per_genre(apple_store_data_cleaned, apple_store_header, index_prime_genre).items(), key=lambda x: x[1], reverse=True);
print(apple_store_data_avg_nbr_rating_per_genre);
print_separator();


# Call the function
avg_installs_per_category(google_play_store_data_cleaned, index_category, index_installs);

# print the average number of installs per category for the Google Play Store
print("\n");
print("Average number of installs per category in Google Play Store: \n");
google_play_store_data_avg_nbr_installs_per_category = sorted(avg_installs_per_category(google_play_store_data_cleaned, index_category, index_installs).items(), key=lambda x: x[1], reverse=True);
print_separator();

               

# split by category
print("\n");
print("Google Play Store - split by category: \n");
google_play_store_data_split_by_category = split_by_column_value(google_play_store_data_cleaned, index_category);
# only print top 3 of each category
for i in google_play_store_data_split_by_category:
    print(i, ":\n");
    print(google_play_store_data_split_by_category[i][:3]);
    print("\n");
print_separator();
print("\n");
print("Apple Store - split by prime genre: \n");
apple_store_data_split_by_prime_genre = split_by_column_value(apple_store_data_cleaned, index_prime_genre);
# only print top 3 of each category
for i in apple_store_data_split_by_prime_genre:
    print(i, ":\n");
    print(apple_store_data_split_by_prime_genre[i][:3]);
    print("\n");

#order each category by number of installs
print("\n");
print("Google Play Store - order each category by number of installs: \n");
google_play_store_data_ordered_by_installs = {};
for i in google_play_store_data_split_by_category:
    google_play_store_data_ordered_by_installs[i] = sorted(google_play_store_data_split_by_category[i], key=lambda x: float(x[index_installs].replace("+", "").replace(",", "")), reverse=True);
    print(i, ":\n");
    print(google_play_store_data_ordered_by_installs[i][:3]);
    print("\n");
print_separator();
print("\n");
print("Apple Store - order each category by number of installs: \n");
apple_store_data_ordered_by_installs = {};
for i in apple_store_data_split_by_prime_genre:
    apple_store_data_ordered_by_installs[i] = sorted(apple_store_data_split_by_prime_genre[i], key=lambda x: float(x[index_rating_count_tot].replace("+", "").replace(",", "")), reverse=True);
    print(i, ":\n");
    print(apple_store_data_ordered_by_installs[i][:3]);
    print("\n");

# sum of installs per category
print("\n");
print("Google Play Store - sum of installs per category: \n");
google_play_store_data_sum_of_installs_per_category = calculate_total_per_category(google_play_store_data_ordered_by_installs, index_installs);
for i in google_play_store_data_sum_of_installs_per_category:
      print(i, ":\n");
      print(google_play_store_data_sum_of_installs_per_category[i]);
      print("\n");
print_separator();
print("\n");
print("Apple Store - sum of installs per category: \n");
apple_store_data_sum_of_installs_per_category = calculate_total_per_category(apple_store_data_ordered_by_installs, index_rating_count_tot);
for i in apple_store_data_sum_of_installs_per_category:
        print(i, ":\n");
        print(apple_store_data_sum_of_installs_per_category[i]);
        print("\n");


#add a column with the app percentage of installs per category (installs / sum of installs per category)
print("\n");
print("Google Play Store - add a column with the app percentage of installs per category: \n");
google_play_store_data_add_percentage = add_percentage_column(google_play_store_data_ordered_by_installs, index_installs);
for i in google_play_store_data_add_percentage:
      print(i, ":\n");
      print(google_play_store_data_add_percentage[i][:3]);
      print("\n");
print_separator();
print("\n");
print("Apple Store - add a column with the app percentage of installs per category: \n");
apple_store_data_add_percentage = add_percentage_column(apple_store_data_ordered_by_installs, index_rating_count_tot)
for i in apple_store_data_add_percentage:
        print(i, ":\n");
        print(apple_store_data_add_percentage[i][:3]);
        print("\n");



