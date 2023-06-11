import sqlite3 as lite

con = lite.connect('usuarios.db')

dados = ['alxntpt', '123456', 'alexandre@email.com', '2196464']

with con:
    cur = con.cursor()
    query = "INSERT INTO cadastro(login, senha, email, celular) VALUES(?, ?, ?, ?)"
    cur.execute(query, dados)