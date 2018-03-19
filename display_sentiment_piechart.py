""" file to display the sentiment analysis of the text, performed in the file doc_sentiment.py """

import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import csv

# open the saved CSV file containing the text keywords against their sentiment analysis
with open('C:/Users/Raees Khan/Desktop/saveddata.csv', 'r', encoding= 'utf8') as csvfile:

    df = pd.read_csv(csvfile)
    sent = df["Sentiment"]  # read the sentiment column

    # count the number of positive, negative and neutral sentiment to display on the pie chart
    count = Counter(sent)
    positive = count['positive']
    negative = count['negative']
    neutral = count['neutral']
    score = count['score']

# labels for the pie chart
labels = 'Positive', 'Negative', 'Neutral'
sizes = [positive, negative, neutral]
colors = ['green', 'red', 'blue']

plt.pie(sizes, labels = labels, colors = colors, shadow = True, startangle= 90)
plt.title("results generated from sentiment analysis from doc_sentiment.py")
plt.show()

# labels for bar graph of sentiment score

labels1 = 'Text', 'Score'
sizes1 = [C[0],'' , C[2]]
colors1 = ['green', 'red']
plt.bar(sizes1, labels = labels1, colors = colors1, shadow = True)
plt.title(" sentiment score based on the polarity confidence")
plt.show()