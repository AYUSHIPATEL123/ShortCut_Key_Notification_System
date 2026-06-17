import sqlite3


DB_PATH = "database/learning.db"

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("""
            UPDATE TASKS SET show_count = 0
""")

conn.commit()

conn.close()
