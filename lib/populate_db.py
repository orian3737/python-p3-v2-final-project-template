from models import init_db, CONN, CURSOR
from models.category import Category
from models.comic import Comic

def populate_db():
    init_db()

    categories = [
        "Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", 
        "Mystery", "Romance", "Sci-Fi", "Thriller"
    ]

    comics = [
        {"title": "Batman: Year One", "issue_number": 1, "category": "Action"},
        {"title": "Spider-Man: Homecoming", "issue_number": 1, "category": "Adventure"},
        {"title": "Deadpool: Merc with a Mouth", "issue_number": 1, "category": "Comedy"},
        {"title": "Watchmen", "issue_number": 1, "category": "Drama"},
        {"title": "The Sandman: Preludes & Nocturnes", "issue_number": 1, "category": "Fantasy"},
        {"title": "Hellboy: Seed of Destruction", "issue_number": 1, "category": "Horror"},
        {"title": "Detective Comics #27", "issue_number": 27, "category": "Mystery"},
        {"title": "Superman: Red Son", "issue_number": 1, "category": "Romance"},
        {"title": "The Infinity Gauntlet", "issue_number": 1, "category": "Sci-Fi"},
        {"title": "Sin City: The Hard Goodbye", "issue_number": 1, "category": "Thriller"}
    ]

    
    for name in categories:
        if Category.find_by_name(name) is None:
            category = Category(name=name)
            category.save()
            print(f"Category '{name}' added.")
        else:
            print(f"Category '{name}' already exists. Skipping.")

   
    for comic in comics:
        category = Category.find_by_name(comic["category"])
        if category:
            try:
                new_comic = Comic(title=comic["title"], issue_number=comic["issue_number"], category=category)
                new_comic.save()
                print(f"Comic '{comic['title']}' added to category '{comic['category']}'.")
            except Exception as e:
                print(f"Error adding comic '{comic['title']}': {e}")
        else:
            print(f"Category '{comic['category']}' not found for comic '{comic['title']}'.")

def view_comics():
    sql = 'SELECT comics.id, comics.title, comics.issue_number, categories.name FROM comics JOIN categories ON comics.category_id = categories.id'
    for row in CURSOR.execute(sql):
        print(f"Comic(id={row[0]}, title='{row[1]}', issue_number='{row[2]}', category='{row[3]}')")

if __name__ == "__main__":
    populate_db()
    print("\nPopulated Comics:")
    view_comics()
