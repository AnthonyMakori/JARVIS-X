import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
c = conn.cursor()

# Create table if not exists
c.execute('''
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT,
    response TEXT
)
''')
conn.commit()

def save_memory(command, response):
    c.execute("INSERT INTO memory (command, response) VALUES (?, ?)", (command, response))
    conn.commit()

def get_recent_memory(limit=5):
    c.execute("SELECT command, response FROM memory ORDER BY id DESC LIMIT ?", (limit,))
    return c.fetchall()
