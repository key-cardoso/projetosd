import mysql.connector
from flask import Flask, request, jsonify

app = Flask('site')


def connect_to_database():
    conn = mysql.connector.connect(
        host='localhotst',
        user='root',
        password='root',
        database='site'
    )
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            ID_usuario INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            sobrenome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            senha VARCHAR(255) NOT NULL.
            celular VARCHAR(255) NOT NULL,
            sexo ENUM('Masclino', 'Femenino', 'Outros')
        )
    ''')
    conn.commit()
    return conn
#Rota para cadastrar usuario
@app.route('/cadastro/usuario', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    sobrenome=request.form['sobrenome']
    email = request.form['email']
    senha = request.form['senha']
    celular=request.form['senha']
    sexo=request.form['Masculino', 'Femenino', 'Outros']

    conn = connect_to_database()
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (nome,sobrenome, email, senha, celular, sexo)
        VALUES (%s, %s, %s, %s,  %s,  %s)
    ''', (nome,sobrenome, email, senha,celular, sexo))
    conn.commit()

    return 'Usuário criado com sucesso'
#rota para consultar CADASTRO
@app.route('/cadastro/<int:ID_usuario>', methods=['GET'])
def get_cadastro(ID_usuario):
    conn = connect_to_database()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM usuarios
        WHERE ID_usuario=%s
    ''', (ID_usuario))
    result = c.fetchone()

    if result:
        return jsonify({
            'ID_usuario': result[0],
            'nome': result[1],
            'sobrenome': result[2]
            'email': result[3],
            'senha': result[4],
            'celular': result[5],
            'sexo': result[6]
        })
    else:
        return jsonify({'message': 'User not found'}), 404

#Rota para login
@app.route('/login/usuario', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['password']
    conn = connect_to_database()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM usuario
        WHERE email=%s AND senha=%s
    ''', (email, senha))
    result = c.fetchone()

    if result:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'}), 401


if 'site' == 'main':
    app.run()
