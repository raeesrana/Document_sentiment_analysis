""" file to clean off HTML tags from the data file to retrieve only the text from the CSV data file """

import csv, os, re    # regex to trim away the HTML tags
import sys

# function to remove HTML tags
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
#os.chdir("D:/pychrm/projects/Twitter sentiment analysis")

doc_set = []

# make a new CSV file to save the trimmed text with removed HTML tags
with io.open('C:/Users/Raees Khan/Desktop/saveddata.csv', 'w', encoding= 'utf8', newline='') as newcsvfile:
    csv_write = csv.writer(newcsvfile)
    csv_write.writerow(["Text"])

# open csv data file to read the text and remove HTML tags
    with open("C:/Users/Raees Khan/Desktop/trimdata.csv", encoding='utf8') as csvfile:
        readersp = csv.reader(csvfile, delimiter = '\t', )


        for i, row in enumerate(readersp):
            if i > 1 and len(row) > 1:

                temp = remove_html_tags(row[1])
                temp = re.sub("[^a-zA-Z]", "", temp)
                Text = doc_set.append(temp)

