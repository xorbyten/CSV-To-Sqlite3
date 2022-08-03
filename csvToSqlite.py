import sqlite3
import sys
import os
import csv

table_name = ""
header = []
rows = []

if len(sys.argv) < 1:
    print("No path for file was provided.")
else:
    #path_to_file = sys.argv[1]
    #path_to_file = "/home/denis/Desktop/os.csv"
    path_to_file = "/home/sined/Desktop/os.csv"
    
    if os.path.exists(path_to_file):
        filename_with_extension = os.path.split(path_to_file)[1]
        table_name = filename_with_extension.split('.')[0]

        print("Opening the file...")
        csv_file = open(path_to_file)
        csv_reader = csv.reader(csv_file)
        print("Getting header from csv file...")
        header = next(csv_reader)
        print("Getting rows from csv file...")
        for row in csv_reader:
            rows.append(row)
        csv_file.close()
        print("The CSV file processed successfully!")

        print("Creating the database...")
        conn = sqlite3.connect("myDatabase.db")
        cursor = conn.cursor()
        print("Creating tables...")
        cursor = conn.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT);")
        print("Adding columns from CSV file to sqlite database...")
        for col in header:
            conn.execute(f"ALTER TABLE {table_name} ADD \"{col}\" TEXT;")
        print("Adding rows from CSV file to sqlite database...")
        header_string = "id, "
        row_string = ""
        for h in header:
            header_string += h + ', '
        header_string = header_string[:-2]
        for r in rows:
            row_string += str(r) + ', '
            row_string = row_string[:-2]
            insert_query = f"INSERT INTO {table_name}({header_string}) VALUES ({row_string})"
            print(insert_query)
            row_string = ""
            insert_query = ""

        conn.close()
    else:
        print("File not found.")