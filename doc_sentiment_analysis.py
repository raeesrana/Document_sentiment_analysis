
""" file to process the text and get the sentiment analysis using the aylien API """

from aylienapiclient import textapi  # aylien API for text sentiment analysis
import csv, io  # to read, write and open csv files


# aylien API ID and Key
application_id = "781305f2"
application_key = "fcdad30830e8a1ac7f26089a218b617a"


client = textapi.Client(application_id, application_key)

# create a new CSV file to write the sentiment output and save to desktop (or defined directory
with io.open('C:/Users/Raees Khan/Desktop/saveddata.csv', 'w', encoding= 'utf8', newline='') as newcsvfile:
    csv_write = csv.writer(newcsvfile)
    csv_write.writerow(["Text", "Sentiment", "Score"])

    # open provided data set CSV file - Base dataset CSV file was too large, so I trimmed it to 13 - 14 rows
    with open("C:/Users/Raees Khan/Desktop/trimdata1.csv", encoding='utf8') as csvfile:
        readersp = csv.reader(csvfile, delimiter = ' ', quotechar = '|' )

        for row in readersp:

            if len(row) == 0:   # if the row is empty in a CSV file, skip it to save alloted limited API calls
                print('skipped')
                continue

            print(' '.join(row))   # print the text in the row

            sentiment = client.Sentiment({'text': row})    #get the sentiment of the text from aylien API
            print(sentiment)    # print the sentiment, subjectivity, confidence etc

            csv_write.writerow([sentiment['text'], sentiment['polarity'], sentiment['polarity_confidence']])   # write the results to the new CSV file with two fields (columns) named text and polarity / sentiment
