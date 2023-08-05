import sqlite3
from .config import *


def connect_db():
    con = sqlite3.connect(get_setting('Index', 'location') + 'movies.db')
    return con


def create_movie_table():
    sql = '''
        CREATE TABLE IF NOT EXISTS movies
            (title TEXT, genre TEXT, imdb FLOAT, runtime TEXT, tomato TEXT, year INT,
             awards TEXT, cast TEXT, director TEXT, poster TEXT, response BOOLEAN, file_info_name TEXT UNIQUE,
              file_info_location TEXT, file_info_ext TEXT)
    '''
    con = connect_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()


def add_movie(data):
    sql = '''
        INSERT OR IGNORE INTO movies
        (title, genre, imdb, runtime, tomato, year, awards, cast, director, poster, 
        response, file_info_name, file_info_location, file_info_ext)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    con = connect_db()
    cur = con.cursor()
    cur.execute(sql, (data['title'], data['genre'], data['imdb'],
                      data['runtime'], data['tomato'], data['year'],
                      data['awards'], data['cast'], data['director'],
                      data['poster'], data['response'], data['file_info']['name'],
                      data['file_info']['location'], data['file_info']['extension']))
    con.commit()

