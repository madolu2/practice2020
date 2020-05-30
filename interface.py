import eel
import sqlite3


conn = sqlite3.connect('database.db')
c = conn.cursor()


@eel.expose
def get_fields(fields):
    try:
        model, color, description, img_url, cost, count = fields
        c.execute(
        f"INSERT INTO autos (model, color, description, img_url, cost, count) VALUES('{model}', '{color}', '{description}', '{img_url}', {cost}, {count});")
        conn.commit()
        return "Отправлено"
    except Exception as e:
        return f"Ошибка - {e}"


eel.init('UIApp')
eel.start('main.html', size=(700, 700))
