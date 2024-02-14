# Coronavirus Twitter Dataset Analysis

## Background

**About the Data:**

Out of 500 million tweets that are sent everyday, about 2% are *geotagged*-that is, the user's device includes the location information
about where the tweets were sent from. In this dataset there are about 1.1 billion tweets that were sent in 2020. The tweets for each day
are stored in a zip file which includes 24 text files. Each tweet in the text files are in JSON format. 

In this project, I was able to analyze the tweet usage during the COVID-19 pandemic utilizing the 1.1 billion tweets that were sent in 2020. 
1. Worked with large scale datasets
2. Worked with multilingual text
3. Used the MapReduce divide-and-conquer paradigm to create parallel code to run on a remote server
4. Practiced data analysis and visualization techniques

**MapReduce Procedure:**

In order to analyze this large dataset, I followed the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze the tweets.
MapReduce is a famous procedure for large scale parallel processing that is widely used in industry. In MapReduce, doubling the number of processors
causes the analysis to take half as long. Thus, this project was done through a remote server with 80 processors, causing the analysis to 
take 80 times faster.

In the mapping step of MapReduce, I processed the zip files for each day of the year in 2020 to `map.py` that allows the data to be performed in parallel.
A shell script file `run_maps.sh` including the nohup command was created to run `map.py` on all of the zip files in 2020 in background. 

To visualize the data that were mapped, I created `reduce.py` which counts the number of times a certain hashtag is called based on which language or 
which country it was tweeted from. Then I created `visualize.py` that plots the data that has been reduced. Another reduce program called `alternative_reduce.py`
was created to count all of the tweets with a specific hashtag over 2020. Then within the same program, it created a line plot that visualized the number of times
the specific hashtag was tweeted per day. 

**Results:** 

The first reduce file `reduce.py` and `visualize.py` created a plot that traced all the hashtags: "#coronavirus" and "#코로나바이러스" and outputted a bar graph
showing the top 10 countries and languages with these hashtags. 

As expected, the US and English were first with "#coronavirus" and Korea and Korean were first with "#코로나바이러스". 

The top 10 countries with '#coronavirus' is shown by this plot:  
![alt text](/plots/coronavirus_country_output_plot.png) 

The top 10 languages with '#coronavirus' is shown by this plot: 
![alt text](/plots/coronavirus_language_output_plot.png)

The top 10 countries with '#코로나바이러스' is shown by this plot:
![alt text](/plots/코로나바이러스_country_output_plot.png)

The top 10 languages with '#코로나바이러스' is shown by this plot: 
![alt text](/plots/코로나바이러스_language_output_plot.png)

The second reduce file `alternative_reduce.py` traced the hashtags: '#coronavirus', 'covid-19', and '#sick' and outputted a line graph that 
showed the usage of these hashtags (count of tweets) per day for the year 2020. 
![alt text](/plots/hashtag_count.png)

