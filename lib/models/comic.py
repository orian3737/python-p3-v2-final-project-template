from models import CONN, CURSOR
from .category import Category

class Comic:
    def __init__(self, title, issue_number, category, id=None):
        self.id = id
        self.title = title
        self.issue_number = issue_number
        self.category = category

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 2 and 50 characters")

    @property
    def issue_number(self):
        return self._issue_number

    @issue_number.setter
    def issue_number(self, value):
        if isinstance(value, int) and value > 0:
            self._issue_number = value
        else:
            raise ValueError("Issue number must be a positive integer")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, Category):
            self._category = value
        else:
            raise ValueError("Category must be an instance of Category class")

    def save(self):
        sql = 'INSERT INTO comics (title, issue_number, category_id) VALUES (?, ?, ?)'
        CURSOR.execute(sql, (self.title, self.issue_number, self.category.id))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def __repr__(self):
        return f"Comic(title='{self.title}', issue_number='{self.issue_number}', category='{self.category.name}')"
