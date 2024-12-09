import sqlite3
from tabulate import tabulate

def get_data():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    return conn, cursor

conn,cursor = get_data()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                year INTEGER NOT NULL,
                description TEXT NOT NULL
               )
               ''')

books = [
    {'title': 'Atomic Habits', 'author': 'James Clear', 'genre': 'Self-Help', 'year': 2018, 'description': "Proven system for \nbuilding good habits.\nBreaking bad ones."},
    {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'genre': 'Fiction', 'year': 1988, 'description': "A shepherd's \njourney to find his\npersonal legend."},
    {'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'genre': 'History', 'year': 2011, 'description': "A brief history of \nhumankind.\nExploring our evolution."},
    {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian', 'year': 1949, 'description': "Totalitarian regime \npracticing surveillance \nand mind control."},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Fiction', 'year': 1960, 'description': "Racial injustice and \nchildhood innocence \nin the Deep South."},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction', 'year': 1925, 'description': "The decay of the American\ndream in the 1920s."},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'Fiction', 'year': 1951, 'description': "A teenager's struggle \nwith the pressures \nof adulthood."},
    {'title': 'Moby Dick', 'author': 'Herman Melville', 'genre': 'Adventure', 'year': 1851, 'description': "Captain Ahab's obsessive\nquest for the white whale."},
    {'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Dystopian', 'year': 1932, 'description': "A society of \nforced conformity and\n artificial happiness."},
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'year': 1954, 'description': "A group battles evil \nforces in a magical,\nepic adventure."},
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'year': 1937, 'description': "Bilbo Baggins embarks on\na quest with dwarves."},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Romance', 'year': 1813, 'description': "Love, class, and \nsocietal expectations in\n19th-century England."},
    {'title': 'The Diary of a Young Girl', 'author': 'Anne Frank', 'genre': 'Biography', 'year': 1947, 'description': "A Jewish girl’s life \nin hiding during\nWorld War II."},
    {'title': 'The Shining', 'author': 'Stephen King', 'genre': 'Horror', 'year': 1977, 'description': "Supernatural horror \nin a remote hotel \nwith a haunted past."},
    {'title': 'Wuthering Heights', 'author': 'Emily Brontë', 'genre': 'Gothic Fiction', 'year': 1847, 'description': "A tragic love story set on\nthe Yorkshire moors."},
    {'title': 'The Handmaid’s Tale', 'author': 'Margaret Atwood', 'genre': 'Dystopian', 'year': 1985, 'description': "Women controlled by the state \nand forced into \nreproductive servitude."},
    {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'genre': 'Dystopian', 'year': 1953, 'description': "Books are banned,\nand firemen burn them \nin this dystopia."},
    {'title': 'The Road', 'author': 'Cormac McCarthy', 'genre': 'Post-Apocalyptic', 'year': 2006, 'description': "A father and son \nstruggle to survive in a \npost-apocalyptic world."},
    {'title': 'The Hitchhiker’s Guide to the Galaxy', 'author': 'Douglas Adams', 'genre': 'Science Fiction', 'year': 1979, 'description': "A humorous space adventure\nacross the galaxy."},
    {'title': 'The Girl on the Train', 'author': 'Paula Hawkins', 'genre': 'Thriller', 'year': 2015, 'description': "A psychological thriller\nabout a missing person's case."}
]

book_tuple = [(book['title'], book['author'], book['genre'], book['year'], book['description']) for book in books]

cursor.executemany('''INSERT INTO books (title, author, genre, year, description)
                      VALUES (?,?,?,?,?)''', book_tuple)

cursor.execute('SELECT * FROM books')
rows = cursor.fetchall()

# Print table with wrapped descriptions
print(tabulate(rows, headers=['ID', 'TITLE', 'AUTHOR', 'GENRE', 'YEAR', 'DESCRIPTION'], tablefmt='fancy_grid'))

conn.commit()
conn.close()
