import sqlite3


conn = sqlite3.connect("chroma_store/chroma.sqlite3")


def get_table_names(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return [row[0] for row in cursor.fetchall()]


table_names = get_table_names(conn)
print("Tables in the database:")
for table_name in table_names:
    print(table_name)

cursor = conn.cursor()
cursor.execute("SELECT * FROM embeddings")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()
