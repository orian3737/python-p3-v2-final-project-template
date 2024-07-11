from helpers import (
    exit_program,
    add_category, 
    search_category,  
    delete_category,
    add_comic,
    search_comic,
    delete_comic 
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_category()
        elif choice == "2":
            search_category()
        elif choice == "3":
            delete_category()
        elif choice == "4":
            add_comic()
        elif choice == "5":
            search_comic()
        elif choice == "6":
            delete_comic()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add Category")
    print("2. Search Category")
    print("3. Delete Category")
    print("4. Add Comic")
    print("5. Search Comic")
    print("6. Delete Comic")

if __name__ == "__main__":
    main()
