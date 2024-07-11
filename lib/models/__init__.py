import sqlite3

CONN = sqlite3.connect('lib/comics.db')
CURSOR = CONN.cursor()

def init_db():
    create_category_table = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    """
    
    create_comic_table = """
    CREATE TABLE IF NOT EXISTS comics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        issue_number INTEGER NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    );
    """
    
    CURSOR.execute(create_category_table)
    CURSOR.execute(create_comic_table)
    CONN.commit()

