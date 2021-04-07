import csv
import cassandra

# Helper functions to drop and create the table.
def drop_table(session, table_name):
    """Drop he table if exists.
    :table_name {str}
    """
    # Drop the table if it exits.
    try:
        session.execute(f"Drop TABLE IF EXISTS {table_name};")
        print(f'>>> Dropped <{table_name}> with success.')
    except Exception as e:
        print(f'>>> Could not drop <{table_name}>;\n{e}')

        
def create_table(session, table_name, query):
    """ Create the table if it doesn't exist.
    :table_name {str}
    :query {str}
    """
    try:
        session.execute(query)
        print(f'>>> Table <{table_name}> created!')
    except Exception as e:
        print(f'>>> Could not create <{table_name}>;\n{e}')

        
def populate_table(session, file_path, query, columns):
    """ Populate the table with appropriate values from the file.
    :session {}
    :file_path {str} the path to the csv file containing the data.
    :query {str} The INSERT query to populate the table.
    :columns {tuple} column numbers in the csvfile
        that gets assigned to the corresponding column in the INSERT query.
    """
    # This is how the format of the 11 columns is expected in the tables.
    col_types = [str, str, str, int, str, float, str, str, int, str, int]
    
    # Read the csv file, and populate the table.
    with open(file_path, encoding = 'utf8') as f:
        print('>>> Populating the table.')
        csvreader = csv.reader(f)
        # Skip the header.
        next(csvreader)
        # Insert the lines into the table.
        for line in csvreader:
            # Assign which column element should be assigned for each column in the INSERT query.
            # For instance: to INSERT artist_name and user first_name,
            # we need to use `line[0], line[1]`
            # Also, convert each value to the appropriate format,
            # based on the table.
            session.execute(query, (col_types[i](line[i]) for i in columns))
        print('Done.')
