# __init__.py
__authors__ = ["tsalazar"]
__version__ = "0.1"

# v0.1 (tsalazar) -- 20180904 Creation.

import logging
import psycopg2
import psycopg2.extras
import pyodbc
import pymongo
import re
import pandas.io.sql as psql
from dataclasses import dataclass
from typing import List, Any


@dataclass
class Database:
    """Interact with MSSQL, PostgreSQL, and MongoDB databases.

    host: Database server hostname or IP.
    port: Database server port.
    database: Database name.
    username: Database server account username.
    password: Database server account password.
    autocommit: Use autocommit on changes?
    dictionary_cursor: Return the results as a dictionary?
    encoding: Database client encoding ("utf8", "latin1", "usascii")
    driver: Database client driver ("postgres", "{MSSQLSERVER}", "FreeTDS", etc.).
    """

    host: str = None
    port: str = None
    database: str = None
    username: str = None
    password: str = None
    autocommit: bool = True
    dictionary_cursor: bool = True
    encoding: str = 'utf8'
    driver: str = None

    def __post_init__(self):

        self.__logger = logging.getLogger(__name__)
        self.__sanity_check()

        self.connection = None

        self.__logger.debug('Establishing connection to the database.')
        if self.driver == 'postgres':
            self.cursor = self.__connect_postgresql()
        elif re.search('^({MSSQL|{SQL |ODBC |FreeTDS)', self.driver):
            self.cursor = self.__connect_mssql()
        elif self.driver == 'mongodb':
            self.cursor = self.__connect_mongodb()

        self.__logger.debug('Database object initialized.')

    def __sanity_check(self):
        """Are we crazy?"""

        assert self.host is not None, self.__logger.critical('No database hostname set.')
        assert self.port is not None, self.__logger.critical('No database port set.')
        assert self.database is not None, self.__logger.critical('No database name set.')
        assert self.username is not None, self.__logger.critical('No database username set.')
        assert self.password is not None, self.__logger.critical('No database password set.')
        assert self.driver is not None, \
            self.__logger.critical('No database driver set. Use sql_server, freetds, postgres')

        self.__logger.debug('Sanity check passed.')

    def __connect_postgresql(self):
        """Connect to a PostgreSQL database"""

        # Try a connection to the database.  If it fails, then log the error and exit
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password,
                client_encoding=self.encoding,
            )

            # If autocommit is set to True, then set it on the connection
            if self.autocommit:
                self.connection.autocommit = True

            # If we want to use a DictCursor, then set it.
            if self.dictionary_cursor:
                return self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            else:
                return self.connection.cursor()

        except psycopg2.Error as e:
            self.__logger.critical('PostgreSQL: error {}'.format(e.pgerror))
            exit(1)

        self.__logger.debug('PostgreSQL database connection established.')

    def __connect_mssql(self):
        """Connect to a MSSQL database."""

        # Try a connection to the database.  If it fails, then log the error and exit
        try:
            connection_string = f'DRIVER={self.driver};SERVER={self.host};DATABASE={self.database};' \
                                f'UID={self.username};PWD={self.password}'

            self.__logger.debug('connection_string: ' + connection_string)

            self.connection = pyodbc.connect(connection_string)
            return self.connection.cursor()

        except ValueError:
            self.__logger.error('MSSQL connection error.')
            exit(1)

        self.__logger.debug('MSSQL database connection established.')

    def __connect_mongodb(self):
        """Connect to a MongoDB database."""

        # Try a connection to the database.  If it fails, then log the error and exit
        try:
            connection_string = \
                f'mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'

            self.__logger.debug('connection_string: ' + connection_string)

            self.connection = pymongo.MongoClient(connection_string)
            return self.connection

        except ValueError:
            self.__logger.error('MongoDB connection error.')
            exit(1)

        self.__logger.debug('MSSQL database connection established.')

    def execute(self, sql_query: str, dataframe: bool = False) -> Any:
        """Execute a SQL query

        :param sql_query: SQL query to execute.
        :param dataframe: Output the results as a dataframe?
        :return: SQL query results as array or dataframe (if dataframe == True).
        """

        self.__logger.debug('Executing query.')
        assert sql_query is not None, self.__logger.critical('sql_query is missing!')

        self.__logger.debug('sql_query:')
        self.__logger.debug(sql_query)

        if dataframe is True:
            return psql.read_sql_query(sql_query, self.connection)
        else:
            self.cursor.execute(sql_query)
            return self.cursor.fetchall()

    def get_header(self) -> List[str]:
        """Return the column headers

        :return: Column headers
        """

        self.__logger.debug('Getting headers from results.')

        # header = [column[0].replace('_', ' ').title() for column in self.cursor.description]
        header = [column[0] for column in self.cursor.description]

        self.__logger.debug('header:')
        self.__logger.debug(header)

        return header
