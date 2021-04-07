# Project: Data Warehouse
## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, I am tasked with building an ETL pipeline that extracts their data from __S3__, stages them in __Redshift__, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

## Project Description
In this project, I'll apply my data warehouses and AWS knowledge to build an ETL pipeline for a database hosted on Redshift. To complete the project, I will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

## Project Datasets
I'll be working with two datasets that reside in S3: `song_data` & `log_data`. A sample `song_data` is like:   

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

And `log_data` sample is like: 
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

## Files Description
- `sql_queries.py`
- `create_tables.py`
- `etl.ipynb`
- `etl.py`
