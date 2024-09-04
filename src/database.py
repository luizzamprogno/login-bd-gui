import sqlite3
import bcrypt

def create_connection():
    return sqlite3.connect('cadastro.db')

def define_cursor(conexao):
    return conexao.cursor()

def create_table(conexao, cursor):

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL
        );
    
    ''')

    conexao.commit()

def hash_password(user_password):

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(user_password.encode('utf-8'), salt)

def verify_password(given_password, hashed_password):

    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(given_password.encode('utf-8'), hashed_password)

def create_new_user(conexao, cursor, new_user, new_password):

    cursor.execute('''
        SELECT *
        FROM Usuarios
        WHERE nome = ?

    ''', (new_user,))

    result = cursor.fetchone()

    if result:
        return False

    else:

        hashed_password = hash_password(new_password)
        
        cursor.execute('''

            INSERT INTO Usuarios (nome, senha)
            VALUES  (?, ?)

        ''', (new_user, hashed_password))
        conexao.commit()

        return True

def login(conexao, cursor, user, password):

    cursor.execute('''
        SELECT senha 
        FROM Usuarios 
        WHERE nome = ?
    
    ''', (user,))

    result = cursor.fetchone()

    if result is None:
        return False

    stored_password = result[0]

    if verify_password(password, stored_password): 
        return True
    else:
        return False