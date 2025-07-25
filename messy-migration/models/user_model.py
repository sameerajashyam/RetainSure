from db.db import get_db

def get_all_users():
    db = get_db()
    return db.execute("SELECT * FROM users").fetchall()

def get_user_by_id(user_id):
    db = get_db()
    return db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

def create_user(name, email, hashed_password):
    db = get_db()
    db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_password))
    db.commit()

def update_user(user_id, name, email):
    db = get_db()
    db.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    db.commit()

def delete_user(user_id):
    db = get_db()
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()

def search_users_by_name(name):
    db = get_db()
    return db.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',)).fetchall()

def get_user_by_email(email):
    db = get_db()
    return db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
