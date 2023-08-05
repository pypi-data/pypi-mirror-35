## functions libary file for all functions that can be used to work with sqlite3 databases
#
# @file		    sqlite3.py
# @author	    Tobias Ecklebe
# @date		    10.08.2018
# @version	    0.1.0
# @note		    To use this file:  from pylibcklb.database.sqlite3 import SomeClassOrFunction\n     
#               
# @pre          The library was developed with python 3.6 64 bit 
#
# @bug          No bugs at the moment.
#
# @copyright    pylibcklb package
#               Copyright (C) 2017  Tobias Ecklebe
#
#               This program is free software: you can redistribute it and/or modify
#               it under the terms of the GNU Lesser General Public License as published by
#               the Free Software Foundation, either version 3 of the License, or
#               (at your option) any later version.
#
#               This program is distributed in the hope that it will be useful,
#               but WITHOUT ANY WARRANTY; without even the implied warranty of
#               MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#               GNU Lesser General Public License for more details.
#
#               You should have received a copy of the GNU Lesser General Public License
#               along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import sqlite3
from sqlite3 import Error
import os

#http://www.sqlitetutorial.net/sqlite-python/create-tables/
def create_connection(db_file:str=None):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        if db_file is None:
            print('Connect to sqlite database in memory')
            conn = sqlite3.connect(':memory:')
        else:
            print('Connect to sqlite database on harddrive')
            conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None
 

#http://www.sqlitetutorial.net/sqlite-python/create-tables/
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        conn.rollback()
        print(e)

def insert_data(conn, sql_statement, args_as_tuple):
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_statement, args_as_tuple)
            conn.commit()
            return c.lastrowid
        except Error as e:
            conn.rollback()
            print(e)
            return None
    else:
        print("Error! cannot create the database connection.")
        return None