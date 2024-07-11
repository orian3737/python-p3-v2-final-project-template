from models import CONN, CURSOR
from models.category import Category
from models.comic import Comic

def add_category():
    name = input("Enter category name: ")
    try:
        category = Category(name=name)
        category.save()
        print(f"Category '{name}' added.")
    except ValueError as e:
        print(f"Error: {e}")

def search_category():
    name = input("Enter category name to search: ")
    category = Category.find_by_name(name)
    if category:
        print(f"Category(id={category.id}, name='{category.name}')")
        sql = 'SELECT * FROM comics WHERE category_id = ?'
        CURSOR.execute(sql, (category.id,))
        comics = CURSOR.fetchall()
        if comics:
            for row in comics:
                print(f"Comic(id={row[0]}, title='{row[1]}', issue_number='{row[2]}', category_id='{row[3]}')")
        else:
            print("No comics found in this category.")
    else:
        print("Category not found.")

def delete_category():
    name = input("Enter category name to delete: ")
    category = Category.find_by_name(name)
    if category:
        sql = 'DELETE FROM categories WHERE name = ?'
        CURSOR.execute(sql, (name,))
        CONN.commit()
        print(f"Category '{name}' deleted.")
    else:
        print("Category not found.")

def add_comic():
    title = input("Enter comic title: ")
    issue_number = input("Enter issue number: ")
    category_name = input("Enter category name: ")

    category = Category.find_by_name(category_name)
    if not category:
        print("Category not found.")
        return

    try:
        comic = Comic(title=title, issue_number=int(issue_number), category=category)
        comic.save()
        print(f"Comic '{title}' added to category '{category_name}'.")
    except ValueError as e:
        print(f"Error: {e}")

def search_comic():
    title = input("Enter comic title to search: ")
    sql = """
    SELECT comics.id, comics.title, comics.issue_number, categories.name 
    FROM comics 
    JOIN categories ON comics.category_id = categories.id
    WHERE comics.title = ?
    """
    CURSOR.execute(sql, (title,))
    comic = CURSOR.fetchone()
    if comic:
        print(f"Comic(id={comic[0]}, title='{comic[1]}', issue_number='{comic[2]}', category='{comic[3]}')")
    else:
        print("Comic not found.")

def delete_comic():
    title = input("Enter comic title to delete: ")
    sql = 'SELECT * FROM comics WHERE title = ?'
    CURSOR.execute(sql, (title,))
    comic = CURSOR.fetchone()
    if comic:
        sql = 'DELETE FROM comics WHERE title = ?'
        CURSOR.execute(sql, (title,))
        CONN.commit()
        print(f"Comic '{title}' deleted.")
    else:
        print("Comic not found.")

def exit_program():
    print("Goodbye!")
    exit()
