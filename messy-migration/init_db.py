import sqlite3
from werkzeug.security import generate_password_hash

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Creating  the users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Sample users with hashed passwords
    sample_users = [
        ('John Doe', 'john@example.com', 'password123'),
        ('Jane Smith', 'jane@example.com', 'secret456'),
        ('Bob Johnson', 'bob@example.com', 'qwerty789'),
    ]

    for name, email, plain_password in sample_users:
        try:
            hashed_password = generate_password_hash(plain_password)
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (name, email, hashed_password)
            )
        except sqlite3.IntegrityError:
            print(f"[INFO] User '{email}' already exists. Skipping insert.")

    conn.commit()
    conn.close()
    print(" Database initialized with sample data.")

if __name__ == '__main__':
    init_db()
