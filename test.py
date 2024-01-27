# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: andrefrancisco <andrefrancisco@student.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/27 18:38:38 by andrefranci       #+#    #+#              #
#    Updated: 2024/01/27 19:26:18 by andrefranci      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mobile_app_data_analysis import *

# Sample dataset
sample_dataset = [
    ["App 1", "Free", "English", "10", "1000"],
    ["App 2", "0", "English", "5", "500"],
    ["App 3", "Paid", "Non-English", "8", "800"],
    ["App 1", "Free", "English", "15", "1500"],
    ["App 4", "Free", "English", "20", "2000"],
    ["App 5", "0.0", "English", "25", "2500"],
    ["App 6", "Free", "çç", "30", "3000"],
]

# Sample header
sample_header = ["App", "Price", "Language", "Reviews", "Installs"]

# Test the functions
cleaned_dataset = check_row_and_delete(sample_dataset, sample_header, "Sample Dataset")

# Print the cleaned dataset
print("\nCleaned Dataset:")
for row in cleaned_dataset:
    print(row)