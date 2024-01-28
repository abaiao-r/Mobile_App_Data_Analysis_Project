# Mobile App Data Analysis Project
This initiative involves a comprehensive exploration of mobile app trends using datasets from Google Play and the App Store. By analyzing genres, categories, and user ratings, we aim to reveal critical patterns.

## Introduction

In this project, we will delve into datasets from the Google Play Store and the Apple App Store. The objective of this project is to analyze datasets for apps available on both the Google Play Store and Apple Store. The focus is on identifying characteristics that contribute to higher user attraction, as the revenue model relies on in-app ads for free downloads. In essence, the goal is to help developers discern the types of apps that are more likely to garner increased user engagement and, consequently, higher revenue through ad interactions.

## Key Points

1. **Platform Diversity:** Analyze data from both Google Play and the App Store to gain a comprehensive understanding of the mobile app landscape.

2. **Revenue Model:** Explore the relationship between app success and in-app advertisements, focusing on factors that drive user engagement.

3. **User Preferences:** Investigate app genres, categories, and user ratings to identify patterns that can guide the development team in creating apps tailored to user preferences.

4. **Decision-Making Support:** Provide actionable insights derived from data analysis to aid developers in making strategic decisions that maximize user reach and enhance ad revenue.

5. **Competitive Edge:** Utilize data-driven decision-making as a powerful tool to stay competitive in the dynamic and evolving field of mobile app development.

## Project Relevance

In the dynamic landscape of mobile app development, understanding user behavior and preferences is crucial for success. By leveraging data analysis techniques, this project aims to equip our development team with valuable insights. These insights will empower them to make informed decisions, ultimately leading to the creation of apps that have the potential to attract a larger user base and maximize ad revenue. This project serves as a comprehensive exploration of the intersection between data analytics and strategic decision-making in the context of mobile app development.


### Data Cleaning Process

So far, our focus has been on refining the data to ensure accuracy and relevance. The following steps have been taken during the cleaning process:

1. **Removed Inaccurate Data:** Any entries containing inaccurate information were carefully identified and removed to maintain data integrity.

2. **Eliminated Duplicate App Entries:** Duplicate app entries were identified and removed to avoid skewing the analysis with redundant information.

3. **Excluded Non-English Apps:** To narrow down our analysis to English-speaking markets, we removed apps in languages other than English.

4. **Isolated Free Apps:** Since our goal is to analyze and determine successful app profiles for revenue generation, we isolated the dataset to include only free apps.

## Validation Strategy

Our validation strategy for app ideas consists of a three-step process to minimize risks and overhead:

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

Remember, these conclusions are based on the number of apps available in each genre, not on their popularity or profitability. To make a recommendation for an app profile, more data and analysis would be needed.

### Most Popular Apps by Genre on the App Store

One way to find out what genres are the most popular (have the most users) is to calculate the average number of installs for each app genre. For the Google Play data set, we can find this information in the Installs column, but for the App Store data set, this information is missing. As a workaround, we'll take the total number of user ratings as a proxy, which we can find in the rating_count_tot app.

Below, we calculate the average number of user ratings per app genre on the App Store:

On average, navigation apps have the highest number of user reviews, but this figure is heavily influenced by Waze and Google Maps, which have close to half a million user reviews together:

However, this niche is dominated by a few giants who are almost impossible to compete with. The same pattern applies to social networking apps, where a few big players like Facebook, Pinterest, Skype, etc. dominate the market. The same applies to music apps, where a few big players like Pandora, Spotify, and Shazam dominate the market.

Our aim is to find popular genres, but navigation, social networking, or music apps might seem more popular than they really are. The average number of ratings seems to be skewed by very few apps that are the giants in their respective markets. These markets seem to show potential, but it's hard to recommend an app profile based on this data alone.

The genres with the highest average number of user ratings, which could be interpreted as popularity, are 'Navigation', 'Reference', and 'Social Networking'.

However, creating an app in these genres doesn't guarantee success, as these markets could be dominated by a few big players. For example, the 'Navigation' genre could be heavily influenced by apps like Google Maps and Waze.

On the other hand, genres like 'Reference', 'Weather', 'Food & Drink', or 'Finance' could be interesting to explore. They have a high average number of user ratings and could offer opportunities for practical apps that serve a purpose, rather than entertainment or social networking apps.

### Most Popular Apps by Genre on Google Play

For the Google Play market, we have data about the number of installs, so we should be able to get a clearer picture about genre popularity. However, the install numbers don't seem precise enough — we can see that most values are open-ended (100+, 1,000+, 5,000+, etc.):
```
print(display_table(android_final, 5)) # the Installs columns
```
```
1,000,000+ : 15.726534296028879
100,000+ : 11.552346570397113
10,000,000+ : 10.548285198555957
10,000+ : 10.198555956678701
1,000+ : 8.393501805054152
100+ : 6.915613718411552
5,000,000+ : 6.825361010830325
500,000+ : 5.561823104693141
50,000+ : 4.7721119133574
5,000+ : 4.512635379061372
10+ : 3.5424187725631766
500+ : 3.2490974729241873
50,000,000+ : 2.3014440433213
100,000,000+ : 2.1322202166064983

```
One problem with this data is that it's not precise. For instance, we don't know whether an app with 100,000+ installs has 100,000 installs, 200,000, or 350,000. However, we don't need very precise data for our purposes — we only want to get an idea which app genres attract the most users, and we don't need perfect precision with respect to the number of users.

We're going to leave the numbers as they are, which means that we'll consider that an app with 100,000+ installs has 100,000 installs, and an app with 1,000,000+ installs has 1,000,000 installs, and so on.

To perform computations, however, we'll need to convert each install number to float — this means that we need to remove the commas and the plus characters, otherwise the conversion will fail and raise an error. We'll do this directly in the loop below, where we also compute the average number of installs for each genre (category).

Below, we calculate the average number of installs per app genre for the Google Play data set:

On average, communication apps have the most installs: 38,456,119. This number is heavily influenced by a few apps that have over one billion installs (WhatsApp, Facebook Messenger, Skype, Google Chrome, Gmail, and Hangouts), and a few others with over 100 and 500 million installs:

If we removed all the communication apps that have over 100 million installs, the average would be reduced roughly ten times:

We see the same pattern for the video players category, which is the runner-up with 24,727,872 installs. The market is dominated by apps like Youtube, Google Play Movies & TV, or MX Player. The pattern is repeated for social apps (where we have giants like Facebook, Instagram, Google+, etc.), photography apps (Google Photos and other popular photo editors), or productivity apps (Microsoft Word, Dropbox, Google Calendar, Evernote, etc.).

Again, the main concern is that these app genres might seem more popular than they really are. Moreover, these niches seem to be dominated by a few giants who are hard to compete against.

The game genre seems pretty popular, but previously we found out this part of the market seems a bit saturated, so we'd like to come up with a different app recommendation if possible.

The books and reference genre looks fairly popular as well, with an average number of installs of 8,767,811. It's interesting to explore this in more depth, as we found this genre has some potential to work well on the App Store, and our aim is to recommend an app genre that shows potential for being profitable on both the App Store and Google Play.

Let's take a look at some of the apps from this genre and their number of installs:

The book and reference genre includes a variety of apps: software for processing and reading ebooks, various collections of libraries, dictionaries, tutorials on programming or languages, etc. It seems there's still a small number of extremely popular apps that skew the average:

However, it looks like there are only a few very popular apps, so this market still shows potential. Let's try to get some app ideas based on the kind of apps that are somewhere in the middle in terms of popularity (between 1,000,000 and 100,000,000 downloads):

This niche seems to be dominated by software for processing and reading ebooks, as well as various collections of libraries and dictionaries, so it's probably not a good idea to build similar apps since there'll be some significant competition.

We also notice there are quite a few apps built around the book Quran, which suggests that building an app around a popular book can be profitable. It seems that taking a popular book (perhaps a more recent book) and turning it into an app could be profitable for both the Google Play and the App Store markets. However, it looks like the market is already full of libraries, so we need to add some special features besides the raw version of the book. This might include daily quotes from the book, an audio version of the book, quizzes on the book, a forum where people can discuss the book, etc.

Looking at the average number of installs per category in the Google Play Store, the categories with the highest averages are 'COMMUNICATION', 'VIDEO_PLAYERS', 'SOCIAL', 'PHOTOGRAPHY', and 'PRODUCTIVITY'.

However, it's important to note that these categories might be heavily influenced by a few giants (like WhatsApp in 'COMMUNICATION', YouTube in 'VIDEO_PLAYERS', Facebook in 'SOCIAL', Google Photos in 'PHOTOGRAPHY', and Google Drive in 'PRODUCTIVITY').

If we aim to find a category that is less dominated by major apps and thus potentially easier to enter, we might look at categories like 'ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 'BOOKS_AND_REFERENCE', and 'EDUCATION'.

For example, 'BOOKS_AND_REFERENCE' could be a promising category. An app in this category could be profitable on both Google Play and the App Store, as it could appeal to a wide audience and could be monetized through in-app purchases and ads.

Please note that this is a high-level analysis and a more detailed analysis might be needed to make a final decision.  

## Conclusion

In this project, we analyzed data about the App Store and Google Play mobile apps with the goal of recommending an app profile that can be profitable for both markets.

We concluded that taking a popular book (perhaps a more recent book) and turning it into an app could be profitable for both the Google Play and the App Store markets. The markets are already full of libraries, so we need to add some special features besides the raw version of the book. This might include daily quotes from the book, an audio version of the book, quizzes on the book, a forum where people can discuss the book, etc.

