# Project: Data Modeling with Postgres

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like to create a Postgres database with tables designed to optimize queries on song play analysis. Your role is to create a __database schema__ and __ETL pipeline__, with Python, for this analysis. 

## Project Description
To complete the project, you will need to __define fact and dimension tables__ for a __star schema__ for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.
![ERD diagram]("./erd-diagram.png")

## File descriptions
`sql_queries.p` contains all the sql queries; the queries here will be used to create the tables, and in ETL pipeline.   
`create_tables.py` drops and creates the tables. Run this file to reset the tables before running the ETL script.
`etl.ipynb` reads and processes a single file from `song_data` and `log_data` and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
`etl.py` reads and processes files from `song_data` and `log_data` and loads them into tables.
`test.ipynb` displays the first few rows of each table to check the database.

## Project Interface
1. You need to create the tables, run `python create_tables.py`.
2. Run `python etl.py` to read the `song_data` and `log_data`, perform cleaning and populate the various tables. 

## Libraries
- psycopg2
- pandas
