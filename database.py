import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="BSmart12300!",
        database="sistema_usuarios"
    )

def create_user(nome, email, senha):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
    conn.commit()
    conn.close()

def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios")
    users = cursor.fetchall()
    conn.close()
    return users

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_user(user_id, nome, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nome = %s, email = %s WHERE id = %s", (nome, email, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
    conn.commit()
    conn.close()