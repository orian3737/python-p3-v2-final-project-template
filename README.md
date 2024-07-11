# Comic Book Manager

## Overview

The Comic Book Manager is a Command-Line Interface (CLI) app that I designed to help fellow NERDS manage their comic book collections. You can add, search, and delete comics and categories, and list comics under specific categories.

## Features

- Add, search, and delete categories.
- Add, search, and delete comics.
- Comics are associated with specific categories.
- User-friendly CLI with clear prompts and input validation.

## Requirements

- Python 3.x
- A basic knowledge of CLI applications
- A basic knoledge of SQLITE 3

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using `pipenv install`.

## Usage

1. Intialize shell: `pipenv shell`
2. Initialize the database: `python lib/cli.py`.
3. Follow the on-screen prompts to manage categories and comics.

   - **0. Exit the program**: Exits the CLI.
    - **1. Add Category**: Prompts you to enter a category name and adds it to the database.
    - **2. View Categories**: Displays all categories in the database.
    - **3. Delete Category**: Prompts you to enter a category name and deletes it from the database.
    - **4. Add Comic**: Prompts you to enter a comic title, issue number, and category name, then adds the comic to         the specified category.   

    - **5. View Comics**: Displays all comics in the database along with their categories.
    - **6. Delete Comic**: Prompts you to enter a comic title and deletes it from the database.

## Category examples

- **Add a Category**:
  - Choose option `1`.
  - Enter `name` when prompted.
  - Output: `Category 'name' added.`

- **View Categories**:
  - Choose option `2`.
  - Output: 
    ```
    Category(id=1, name='Fantasy')
    ```2

- **Add a Comic**:
  - Choose option `4`.
  - Enter `The Sandman` for the title, `1` for the issue number, and `Fantasy` for the category name.
  - Output: `Comic 'The Sandman' added to category 'Fantasy'.`

- **View Comics**:
  - Choose option `5`.
  - Output:
    ```
    Comic(id=1, title='The Sandman', issue_number='1', category='Fantasy')
    ```

- **Delete a Comic**:
  - Choose option `6`.
  - Enter `The Sandman` when prompted.
  - Output: `Comic 'The Sandman' deleted.`

- **Delete a Category**:
  - Choose option `3`.
  - Enter `Fantasy` when prompted.
  - Output: `Category 'Fantasy' deleted.`
## Project Structure

- `models/`: Contains the database models.
- `cli/`: Contains the CLI logic.
- `main.py`: Entry point of the application.
- `README.md`: Project documentation.

