
# Import libraries.
import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """ Process song json files.
    Populate the songs and artists tables.
    :filepath {str} path to json file.
    :cur {cursor}
    """
    # open song file
    dfsong = pd.read_json(filepath, lines= True)
    
    # Round the song duration to nearest integer.
    dfsong['duration'] = dfsong['duration'].round().astype('int')

    # insert song record
    cols_song = ['song_id', 'title', 'artist_id', 'year', 'duration']
    song_data = dfsong[cols_song].values.tolist()[0]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    cols = ['id', 'name', 'location', 'latitude', 'longitude']
    # Add the prefix.
    cols_artist = ['artist_' + col for col in cols]
    artist_data = dfsong[cols_artist].values.tolist()[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """ Process log json files.
    Populate the following tables:
    -- time, users, songplays
    :filepath {str} path to json file.
    :cur {cursor}
    """
    # Read the json file.
    dflog = pd.read_json(filepath, lines= True)

    # Filter by NextSong action.
    dflog = dflog[dflog['page'] == 'NextSong']
    
    # Round the song duration/length to nearest integer.
    dflog['length'] = dflog['length'].round().astype('int')
    
    # Convert timestamp column to datetime
    dflog['time_stamp'] = pd.to_datetime(dflog['ts'], unit= 'ms')
    # Get these columns: hour, day, week, month, year, weekday
    dflog['hour'] = dflog['time_stamp'].dt.hour
    dflog['day'] = dflog['time_stamp'].dt.day
    dflog['week'] = dflog['time_stamp'].dt.week
    dflog['month'] = dflog['time_stamp'].dt.month
    dflog['year'] = dflog['time_stamp'].dt.year
    dflog['weekday'] = dflog['time_stamp'].dt.weekday
    
    cols_time = ['time_stamp', 'hour', 'day', 'week',
                 'month', 'year', 'weekday']
    time_data = dflog[cols_time].values.tolist()
    for log in time_data:
        cur.execute(time_table_insert, log)

    # Load user table: =======================================
    cols_user = ['userId', 'firstName', 'lastName', 'gender', 'level']
    df_user = dflog[cols_user].copy()
    # Remove the rows that `userId` is empty string or NaN.
    # df_user = df_user[df_user['userId'] != '']
    df_user = df_user.loc[df_user['userId'].notna()]
    # Convert userId to integer.
    df_user['userId'] = df_user['userId'].astype('int')

    # insert user records
    for _, row in df_user.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for _, row in dflog.iterrows():
        # Get song_id and artist_id from song and artist tables.
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None

        # insert songplay record
        songplay_data = (row['time_stamp'], row['userId'], row['level'],
                         song_id, artist_id,
                         row['sessionId'], row['location'], row['userAgent'])
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """Auxiliary function to process json files."""
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print(f'\n{num_files} files found in {filepath}')

    # iterate over files and process
    for i, datafile in enumerate(all_files, start= 1):
        func(cur, datafile)
        conn.commit()
        if i % 10 == 0:
            print(f'{i}/{num_files} files processed.')


def main():
    q = "host=127.0.0.1 dbname=sparkifydb user=student password=student"
    conn = psycopg2.connect(q)
    cur = conn.cursor()
    
    # Process song_data.
    process_data(cur, conn, filepath= 'data/song_data',
                 func= process_song_file)
    # Process log data.
    process_data(cur, conn, filepath= 'data/log_data',
                 func= process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
