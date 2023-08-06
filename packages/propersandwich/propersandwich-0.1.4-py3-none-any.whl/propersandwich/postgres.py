"""
This module will help to perform CRUD operations with Postgres databases
"""

import psycopg2
from dotenv import load_dotenv
import os
import io
import logging
import pandas as pd

load_dotenv()


def connection(database):
    """
    Create a session with a given database and return a new connection object.


    :param str database: the name of the database that will be used as prefix to get its credentials

    :returns: connection object
    :rtype: connection

    """

    dbname = os.getenv(f'{database}_DBNAME')
    user = os.getenv(f'{database}_USER')
    password = os.getenv(f'{database}_PASSWORD')
    host = os.getenv(f'{database}_HOST')
    port = os.getenv(f'{database}_PORT')

    return psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)


def query(database, sql_query) -> list:
    """
    Run a query against a database then returns it's result as a list


    :param str database: the name of the database that will be used as prefix to get its credentials
    :param str sql_query: The sql query that will be executed

    :returns: a list of records
    :rtype: list

    """
    try:
        conn = connection(database)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        data = cursor.fetchall()

        # Convert the data to a dataframe
        df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])

    except (Exception, psycopg2.Error) as error:
        logging.error(f'Error while executing query on {database} database', error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            logging.info(f'The connection to {database} database is now closed')

    return df


def destructive_write(database, table, data) -> bool:
    """
    Overwrite the contents of a postgres database table with new data.

    :param str database: The name of the database.
    :param str table: The name of the table.
    :param pd.Dataframe data: The dataframe that contains the data to write to the table.

    :return: True if the write was successful, False otherwise.
    :rtype: bool

    """

    try:
        conn = connection(database)
        cursor = conn.cursor()

        # Drop table if it exists
        cursor.execute(f'DROP TABLE IF EXISTS {table}')
        conn.commit()

        # Create table
        column_defs = ", ".join([f"{col} {_get_postgres_type(data[col].dtype)}" for col in data.columns])
        if column_defs:
            column_defs = f"index integer, {column_defs}"
        cursor.execute(f'CREATE TABLE {table} ({column_defs})')
        conn.commit()

        # Insert data
        output = io.StringIO()
        data.to_csv(output, sep=';', header=False, index=True)
        output.seek(0)
        output.getvalue()
        cursor.copy_from(output, table, sep=';', null='')
        conn.commit()
        logging.info(f'The data has been written to {table} table')

    except (Exception, psycopg2.Error) as error:
        logging.error(f'Error while executing query on {database} database', error)
        return False

    finally:
        if conn:
            cursor.close()
            conn.close()
            logging.info(f'The connection to {database} database is now closed')
    return True


def _get_postgres_type(dtype):
    """
    Map a pandas dtype to a PostgreSQL type.

    :param dtype dtype: The dtype to map.

    :return: The corresponding PostgreSQL type.
    :rtype: str
    """
    if dtype == 'int64':
        return 'bigint'
    elif dtype == 'float64':
        return 'double_precision'
    elif dtype == 'bool':
        return 'boolean'
    else:
        return 'text'
