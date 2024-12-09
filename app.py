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

conn.commit()
conn.close()

def view_Books():
    conn,cursor = get_data()

    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()

    print(tabulate(rows,headers=['ID','TITLE','AUTHOR','GENRE','YEAR','DESCRIPTION'],tablefmt='fancy_grid'))
    conn.commit()
    conn.close()

def add_Books():
    conn,cursor = get_data()

    title = input("Enter title of the book: ")
    author = input("Enter author of the book: ")
    genre = input("Enter author of the book: ")
    year = int(input("Enter author of the book: "))
    description = input("Enter description of the book: ")

    cursor.execute('INSERT INTO books (title, author, genre, year, description) VALUES (?,?,?,?,?)', (title,author,genre,year,description))

    conn.commit()
    conn.close()

def searchBook():
    user_input= input('''
Which genre book you want to search
1. Self-Help
2. Fiction
3. History
4. Dystopian
5. Romance
6. Gothic Fiction
7. Biography
8. Horror
9. Fantasy
10. Science Fiction
11. Post-Apocalyptic
12. Thriller: \n''')

    conn,cursor = get_data()

    cursor.execute('SELECT * FROM books WHERE genre = ?',(user_input,))
    rows = cursor.fetchall()

    print(tabulate(rows,headers=['ID','TITLE','AUTHOR','GENRE','YEAR','DESCRIPTION'],tablefmt='fancy_grid'))

    conn.close()

def countBooks():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM books')
    count = cursor.fetchone()[0]
    
    print(f"Total number of books: {count}")
    conn.close()

def main():
    while True:
        print("1. View Books \n2. Add Books\n3. Search Book by genre \n4. Count books\n5. Exit")
        choice=int(input("Enter your choice: "))

        if choice == 1:
            view_Books()
        
        elif choice ==2:
            add_Books()

        elif choice==3:
            searchBook()

        elif choice ==4:
            countBooks()

        elif choice == 5:
            print("Exiting: ")
            break

        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()