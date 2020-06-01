import flask
import sqlite3

app = flask.Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('../database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM autos;')
    
    create_dict = lambda line: {
        'id': line[0],
        'model': line[1],
        'color': line[2],
        'description': line[3],
        'img_url': line[4],
        'cost': line[5],
        'count': line[6]
    }

    results = [create_dict(line) for line in c.fetchall()]
    return flask.render_template("index.html", results=results)


app.run(debug=True)
