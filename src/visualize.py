#!/usr/bin/env python3 

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
 
# Plot the bar graph
for k,v in reversed(items[:10]):
    print(k,':',v)
    plt.bar(k, v)

# Setting names for the plot label
if args.input_path.endswith('country'):
    x_label = 'country'
else:
    x_label = 'language'

name = args.key.lstrip('#')

# Labels for bar graph 
plt.title(f'{name}')
plt.xlabel(f'{x_label}')
plt.ylabel('Count of Tweets')
 
# Rotated the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Naming the output file
plt.savefig(f'{name}_{x_label}_output_plot.png')
