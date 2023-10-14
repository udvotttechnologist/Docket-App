import sqlite3
import offline_file_handling as ofh
import psycopg2

def append_db():
    file_name = ofh.read_uid()
    conn = sqlite3.connect(file_name+".db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS todo_list(
            list_item TEXT,
            priority INT4
        );""")
    conn.commit()
    conn.close()

def append_table_for_notification():
    file_name = ofh.read_uid()
    conn = sqlite3.connect(file_name+".db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS notifier(
        list_item TEXT,
        notification_datetime TEXT
);""")
    conn.commit()
    conn.close()

def check_exist(text):
    file = ofh.read_uid()
    conn = sqlite3.connect(file + ".db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT (*) FROM notifier WHERE list_item = (?)",
                   (text,))
    edit_exist = cursor.fetchall()
    return edit_exist[0]

def remove_notification2(item):
    file = ofh.read_uid()
    conn = sqlite3.connect(file + ".db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notifier WHERE list_item = ?", (item,))
    conn.commit()
    conn.close()
