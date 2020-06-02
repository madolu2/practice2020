import flask
import sqlite3

app = flask.Flask(__name__)


@app.route('/main/<username>')
def main_page(username):
    conn = sqlite3.connect('../database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM autos;')

    def create_dict(line): return {
        'id': line[0],
        'model': line[1],
        'color': line[2],
        'description': line[3],
        'img_url': line[4],
        'cost': line[5],
        'count': line[6]
    }

    results = [create_dict(line) for line in c.fetchall()]
    return flask.render_template("index.html", results=results, username=username)


@app.route('/')
def auth_page():
    return flask.render_template("auth.html")


@app.route('/auth', methods=['POST'])
def auth():
    try:
        conn = sqlite3.connect('../database.db')
        c = conn.cursor()
        login, password = eval(flask.request.data)
        c.execute(
            f"SELECT login, pass FROM users WHERE login='{login}' AND pass='{password}';")
        result = c.fetchone()
        print(result, login, password)
        if result is None:
            return f"Такого пользователя или пароля не существует"
        else:
            return f'http://127.0.0.1:5000/main/{login}'
    except sqlite3.OperationalError:
        return f"Такого пользователя или пароля не существует"


@app.route('/reg', methods=['POST'])
def reg():
    try:
        conn = sqlite3.connect('../database.db')
        c = conn.cursor()
        login, password = eval(flask.request.data)
        c.execute(
            f"SELECT login, pass FROM users WHERE login='{login}' AND pass='{password}';")
        if c.fetchone() is None:
            c.execute(
                f"INSERT INTO users (login, pass, bucket) VALUES ('{login}', '{password}', '');")
            conn.commit()
            return flask.redirect(
                flask.url_for('.main_page', username=login)
            )
        else:
            return 'Такой пользователь уже существует'

    except sqlite3.OperationalError:
        return f'{sqlite3.OperationalError}'


app.run(debug=True)
