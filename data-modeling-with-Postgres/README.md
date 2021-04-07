# Project: Data Modeling with Postgres

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like to create a Postgres database with tables designed to optimize queries on song play analysis. Your role is to create a __database schema__ and __ETL pipeline__, with Python, for this analysis. 

## Project Description
To complete the project, you will need to __define fact and dimension tables__ for a __star schema__ for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.   

<img src="erd-diagram.png" alt="ERD Diagram" width="800"/>

## Data Description
There are two sources of data in this project: a sample `song_data` can bee seen bellow. 
```
{'num_songs': 1,
 'artist_id': 'ARD7TVE1187B99BFB1',
 'artist_latitude': None,
 'artist_longitude': None,
 'artist_location': 'California - LA',
 'artist_name': 'Casual',
 'song_id': 'SOQLGFP12A58A7800E',
 'title': 'OAKtown',
 'duration': 259.44771,
 'year': 0}
 ```
    
 The `log_data` is a 
 ```
 {'artist': None,
 'auth': 'Logged In',
 'firstName': 'Kaylee',
 'gender': 'F',
 'itemInSession': 0,
 'lastName': 'Summers',
 'length': None,
 'level': 'free',
 'location': 'Phoenix-Mesa-Scottsdale, AZ',
 'method': 'GET',
 'page': 'Home',
 'registration': 1540344794796.0,
 'sessionId': 139,
 'song': None,
 'status': 200,
 'ts': 1541106106796,
 'userAgent': '"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"',
 'userId': '8'}
 ```

## File Descriptions
- `sql_queries.py` contains all the sql queries; the queries here will be used to create the tables, and in ETL pipeline.    

- `create_tables.py` drops and creates the tables. Run this file to reset the tables before running the ETL script.   

- `etl.ipynb` reads and processes a single file from `song_data` and `log_data` and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.   

- `etl.py` reads and processes files from `song_data` and `log_data` and loads them into tables.   

- `test.ipynb` displays the first few rows of each table to check the database.

## Project Interface
1. You need to create the tables, run `python create_tables.py`.
2. Run `python etl.py` to read the `song_data` and `log_data`, perform cleaning and populate the various tables. 

## Libraries
- psycopg2
- pandas
