# Document_sentiment_analysis


Document Sentiment Analysis Using the Aylien TAP (Text Analysis API)

Use:

1. Remove_HTML_tags_CSV.py – to remove html and css tags from the CSV data set files to obtain pure text for analysis.

2. Doc_sentiment_analysis.py – to load the CSV file and do the sentiment analysis on the text present in CSV file.

3. Display_sentiment_piechart.py – to display the analyzed sentiment in form of a pie chart.

Note: the provided data set was around 500 MBs, which was difficult to process and presented max character limit error, so I trimmed the data set, to 14 rows, and added 2 to 3 random text rows on my own.

Python Libraries and dependencies used:

1. Matplotlib
2. Pandas
3. Collections
4. Csv
5. Sys
6. Regex
7. Aylien API

References and sites used for help:

1. https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
2. https://stackoverflow.com/questions/15063936/csv-error-field-larger-than-field-limit-131072
3. http://fredgibbs.net/tutorials/extract-transform-save-csv
4. https://de.dariah.eu/tatom/topic_model_python.html
5. https://github.com/wesslen/BigDataPatent
6. https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html
7. https://www.dotnetperls.com/remove-html-tags-python
8. http://blog.aylien.com/first-text-mining-project-python-3-steps/
9. https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string

