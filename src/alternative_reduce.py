#!/usr/bin/env python3 

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--hashtags',nargs='+', required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# load each of the input paths and plot the line graph

for hashtag in args.hashtags:
    y_values = []
    for path in args.input_paths:
        with open(path) as f:
            tmp = json.load(f)
            if hashtag in tmp:
                y_values.append(sum(tmp[hashtag].values()))
    x_values = range(len(y_values))
    plt.plot(x_values, y_values, label=f'{hashtag}')

# Labels for bar graph 
plt.xlabel('Days in the Year' )
plt.ylabel('Count of Hashtags')
plt.title('Count of Tweets by Hashtag in 2020')

# Rotated the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Naming the output file
plt.savefig('hashtag_count.png')
