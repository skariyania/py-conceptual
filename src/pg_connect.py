""" in progress - exercise """
import os
import psycopg2

dbname = os.getenv("database_name", "postgres")
user = os.getenv("username", "postgres")
password = os.getenv("password")
host = os.getenv("host", "localhost")
port = os.getenv("port", "5432")

def select_from_reservation():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute("SELECT * FROM public.reservation")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # Close database connection and cursor
        if conn:
            cursor.close()
            conn.close()

# Call the function to execute the query
select_from_reservation()
