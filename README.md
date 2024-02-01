# Mobile App Data Analysis Project
This initiative involves a comprehensive exploration of mobile app trends using datasets from Google Play and the App Store. By analyzing genres, categories, and user ratings, the aim is to reveal critical patterns.

## Introduction

The objective of this project is to analyze datasets for apps available on both the Google Play Store and Apple Store. The focus is on identifying characteristics that contribute to higher user attraction, as the revenue model relies on in-app ads for free downloads. In essence, the goal is to help developers discern the types of apps that are more likely to garner increased user engagement and, consequently, higher revenue through ad interactions.

## Key Points

1. **Platform Diversity:** Analyze data from both Google Play and the App Store to gain a comprehensive understanding of the mobile app landscape.

2. **Revenue Model:** Explore the relationship between app success and in-app advertisements, focusing on factors that drive user engagement.

3. **User Preferences:** Investigate app genres, categories, and user ratings to identify patterns that can guide the development team in creating apps tailored to user preferences.

4. **Decision-Making Support:** Provide actionable insights derived from data analysis to aid developers in making strategic decisions that maximize user reach and enhance ad revenue.

5. **Competitive Edge:** Utilize data-driven decision-making as a powerful tool to stay competitive in the dynamic and evolving field of mobile app development.

## Project Relevance

In the dynamic landscape of mobile app development, understanding user behavior and preferences is crucial for success. By leveraging data analysis techniques, this project aims to equip our development team with valuable insights. These insights will empower them to make informed decisions, ultimately leading to the creation of apps that have the potential to attract a larger user base and maximize ad revenue. This project serves as a comprehensive exploration of the intersection between data analytics and strategic decision-making in the context of mobile app development.

## How to Run the Code

Requirements:
    - Python 3.8.5
    - on the termianl: python3 mobile_app_data_analysis.py

or you can check the code on the jupyter notebook file(/.ipynb_checkpoints/mobile_app_data_analysis_jn-checkpoint.ipynb)

### Data Extraction

In this project two datasets from the Google Play Store and the Apple App Store were used.

These datasets are stored in CSV files, specifically `googleplaystore.csv` and `AppleStore.csv`.

A sript was written to extract this datasets:

1. **Setting up the file paths**: The script starts by setting up the locations of the datasets. These locations are stored in what we call 'file paths'.

2. **Preparing for the data**: The script then sets up 'containers' to hold the datasets and their headers. Headers are the titles of the different categories of data in the datasets.

3. **Opening the datasets**: The script uses a function called `open_csv` to open the datasets. It then stores the data and headers in their respective 'containers'.

4. **Displaying the data**: Finally, the script uses a function called `print_headers_and_datasets` to display the headers and datasets. This allows us to see the data in a structured and organized manner.

This process allow the extraction and view of the data from the Google Play Store and Apple App Store datasets.


### Data Cleaning Process

After extracting the data, it is necessary to refine the data to ensure accuracy and relevance. The following steps have been taken during the cleaning process:

1. **Removed Inaccurate Data:** Any entries containing inaccurate information were carefully identified and removed to maintain data integrity.

2. **Eliminated Duplicate App Entries:** Duplicate app entries were identified and removed to avoid skewing the analysis with redundant information.

3. **Excluded Non-English Apps:** To narrow down our analysis to English-speaking markets, we removed apps in languages other than English.

4. **Isolated Free Apps:** Since our goal is to analyze and determine successful app profiles for revenue generation, we isolated the dataset to include only free apps.

## Validation Strategy

In this scenario, the strategy for the app ideas consists of a three-step process to minimize risks and overhead:

1. **Build a Minimal Android Version:** Develop a basic Android version of the app and release it on Google Play.

2. **User Response Evaluation:** Assess the app's response from users. If the feedback is positive, proceed to the next step.

3. **Further Development and iOS Version:** If the app proves to be profitable after six months, further development is undertaken, and an iOS version is built for inclusion in the App Store.


## Data Analysis

### Most Common Apps by Genre

The following table shows the most common app genres in the App Store:

Based on the output of your script, here are the answers to your questions:

For the App Store dataset, the most common genre is Games (59.14%), followed by Entertainment (7.53%). Most of the apps are designed for entertainment rather than practical purposes. However, this frequency table alone doesn't imply that these genres also have a large number of users. User preference can be different from the number of apps available in each genre.

For the Google Play dataset, the most common genres are Tools (8.57%) and Entertainment (6.09%) for the Genres column, and Family (18.81%) and Game (9.61%) for the Category column. The Google Play market seems to have a more balanced distribution of app genres, with a good mix of practical and entertainment apps.

Comparing the two markets, the App Store is dominated by games and entertainment apps, while the Google Play market has a more balanced landscape of both practical and entertainment apps.

Based on these frequency tables alone, it's hard to recommend an app profile without additional information such as user ratings, number of installs, and revenue data. The frequency tables reveal the most frequent app genres, but not necessarily what genres have the most users or generate the most revenue.

These assumptions are based on the number of apps available in each genre, not on their popularity or profitability. To make a recommendation for an app profile, more data and analysis would be needed.

### Most Popular Apps by Genre on the App Store

One way to find out what genres are the most popular (have the most users) is to calculate the average number of installs for each app genre. For the Google Play data set, we can find this information in the Installs column, but for the App Store data set, this information is missing. As a workaround, we'll take the total number of user ratings as a proxy, which we can find in the rating_count_tot app.

Below, we calculate the average number of user ratings per app genre on the App Store:

# App Popularity Analysis: Google Play Store and Apple App Store

On average, navigation apps appear to have the highest number of user reviews. However, this figure may be skewed by a few apps with hundreds of thousands of reviews, while others struggle to surpass the 10,000 review threshold.

## Python Script Operations Overview

The following Python script performs several operations on the Google Play Store and Apple App Store datasets:

1. **Splitting by Category/Prime Genre:**
   - Datasets are divided into groups based on the app's category (Google Play Store) or prime genre (Apple App Store).
   - The top 3 apps from each category or prime genre are printed.

2. **Ordering by Number of Installs:**
   - Within each category or prime genre, apps are ordered by the number of installs.
   - The top 3 apps with the most installs from each category or prime genre are printed.

3. **Sum of Installs per Category/Prime Genre:**
   - The total number of installs is calculated for each category or prime genre and printed.

4. **Adding a Column for Percentage of Installs per Category/Prime Genre:**
   - A new column is added to the datasets, indicating the percentage of installs that each app has within its category or prime genre.
   - The top 3 apps from each category or prime genre, along with their percentage of installs, are printed.

These operations aim to provide insights into the most popular categories or prime genres, identify apps with the highest installs within each category or prime genre, and illustrate the distribution of installs within each category or prime genre.

Please note that these analyses are based on available data and assumptions, and the interpretation may be influenced by outliers in the number of user reviews or installs.


# Mobile App Analysis: App Store and Google Play

## App Store Genres and Popularity

The goal is to identify popular genres, but genres like navigation, social networking, or music might seem more popular due to a few dominant apps. The average number of ratings is skewed by a handful of giants, making it challenging to recommend an app profile based solely on this data.

Genres with the highest average number of user ratings ('Navigation', 'Reference', and 'Social Networking') might have dominance by a few big players, like Google Maps and Waze. Genres like 'Reference', 'Weather', 'Food & Drink', or 'Finance' could be interesting, offering opportunities for practical apps rather than entertainment or social networking.

## Most Popular Apps by Genre on Google Play

For the Google Play market, install numbers provide clearer insights into genre popularity. However, these numbers are not precise, and categories may be influenced by a few giants. Communication apps have the most installs, heavily influenced by apps like WhatsApp and Facebook Messenger. Similarly, video players, social apps, and productivity apps follow the same pattern, dominated by a few major players.

While game genres seem popular, they may be saturated. 'Books and Reference' genre looks promising, showing potential for profitability on both the App Store and Google Play. A deeper exploration reveals that popular apps in this genre are dominated by a few, leaving room for new apps with unique features.

## App Recommendations

Based on the analysis, building an app around a popular book with additional features like daily quotes, audio versions, quizzes, and discussion forums could be profitable for both markets. The 'Books and Reference' category is a potential choice.

## Category Analysis on Google Play

Looking at the average number of installs per category in the Google Play Store, categories like 'COMMUNICATION', 'VIDEO_PLAYERS', 'SOCIAL', 'PHOTOGRAPHY', and 'PRODUCTIVITY' have high averages. However, these may be heavily influenced by major apps.

For a less dominated category, exploring 'ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 'BOOKS_AND_REFERENCE', and 'EDUCATION' could be worthwhile. 'BOOKS_AND_REFERENCE' stands out as a promising category with potential for a wide audience.

## Conclusion

In conclusion, turning a popular book into an app, enriched with additional features, is recommended for profitability on both App Store and Google Play. The 'Books and Reference' category offers potential, but a more detailed analysis may be needed for a final decision.
