
import sqlite3

connection = sqlite3.connect('data.db')

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries(id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, date TEXT);")

def add_entry(content, date):
    with connection:
        connection.execute("INSERT INTO entries(content, date) VALUES (?, ?)", (content, date))

def get_entries():
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM entries;")
        return cursor

def get_dated_entries(specified_date):
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM entries WHERE date = ? ;", (specified_date,))
        return cursor.fetchall()

def get_last_entry():
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT content, date FROM entries WHERE id =(SELECT MAX(id) FROM entries);")
        return cursor.fetchone()

def del_entry():
    with connection:
        connection.execute("DELETE FROM entries WHERE id =(SELECT MAX(id) FROM entries);")



