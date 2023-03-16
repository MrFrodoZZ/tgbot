import sqlite3

db = sqlite3.connect('db.db')
sql = db.cursor()


def new_user(tg_id):
    sql.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (None, tg_id, None, None))
    db.commit()


def insert_name(tg_id, name):
    sql.execute(f"UPDATE users SET name = {name} WHERE tg_id = {tg_id}")
    db.commit()


def insert_course(tg_id, course):
    sql.execute(f"UPDATE users SET course = (SELECT id FROM courses WHERE name = {course}) WHERE tg_id = {tg_id}")
    db.commit()


def delete_user(name):
    sql.execute(f"DELETE FROM users WHERE name = {name}")
    db.commit()


def delete_self(tg_id):
    sql.execute(f"DELETE FROM users WHERE tg_id = {tg_id}")
    db.commit()


def check_user(tg_id):
    res = sql.execute(f"SELECT * FROM users WHERE tg_id = {tg_id}").fetchone()
    if len(res) == 1:
        return True
    return False


if __name__ == '__main__':
    sql.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER AUTOINCREMET,
                        tg_id INTEGER,
                        name TEXT,
                        course INTEGER)''')
    db.commit()
    sql.execute('''CREATE TABLE IF NOT EXISTS courses (
                        id INTEGER,
                        name TEXT)''')
    db.commit()

db.close()
