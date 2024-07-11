from models import CONN, CURSOR

class Category:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 50:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 50 characters")

    def save(self):
        sql = 'INSERT INTO categories (name) VALUES (?)'
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def __repr__(self):
        return f"Category(name='{self.name}')"

    @staticmethod
    def find_by_name(name):
        sql = 'SELECT * FROM categories WHERE name = ?'
        CURSOR.execute(sql, (name,))
        result = CURSOR.fetchone()
        if result:
            return Category(id=result[0], name=result[1])
        return None
