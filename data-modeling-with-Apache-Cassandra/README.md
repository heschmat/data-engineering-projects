# Project: Data Modeling with Apache Cassandra

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.   

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions. The task is __to create a database for this analysis__. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

## Project Description
To complete the project, I will model the data by creating tables in Apache Cassandra, keeping in mind the queries needed to be run. Then I'll build an ETL pipeline using Python. This will include iterating through a set of event files, in CSV format, creating a streamlined CSV file to model and insert data into Apache Cassandra tables. 

## Data Description
The `event_data` reside in a directory of CSV files on user activity on the app. The directory of CSV files are partitioned by date. Here are examples of filepaths to two files in the dataset:
```
event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv
```
Only the following columns will be used in each file.
```
['artist',
 'firstName',
 'gender',
 'itemInSession',
 'lastName',
 'length',
 'level',
 'location',
 'sessionId',
 'song',
 'userId']
```   

A sample values for such columns is like: 
```
['Jimi Hendrix',
  'Mohammad',
  'M',
  '1',
  'Rodriguez',
  '239.82975',
  'paid',
  'Sacramento--Roseville--Arden-Arcade, CA',
  '961',
  'Woodstock Inprovisation',
  '88']
  ```

## Libraries
- cassandra
- numpy
- pandas


## File Descriptions
`helper.py` helper functions to drop, create and populate the tables.
`etl.ipynb` Iterates through each event file  and generates a single csv file - `event_datafile_new.csv`. This notebook contains detailed instructions about the ETL processes for each of the tables.
`event_datafile_new.csv` 
