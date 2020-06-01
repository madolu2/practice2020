import random as r
import sqlite3

сolors = ['голубой', 'серый', 'черный', 'фиолетовый', 'красный', 'желтый']
description = 'Описание, которое мне лень делать, но которое формально существует'
autos = [('Hyundai Solaris', 'https://upload.wikimedia.org/wikipedia/commons/6/63/Hyundai_Solaris_%28HC%29.jpg'),
         ('Hyundai Creta', 'https://upload.wikimedia.org/wikipedia/commons/3/3f/Hyundai_Creta.jpg'),
         ('Skoda Kodiaq', 'https://upload.wikimedia.org/wikipedia/commons/0/0b/2018_Skoda_Kodiaq_Scout_TDi_SCR_4X4_2.0_Front.jpg'),
         ('Kia Optima', 'https://s0.rbk.ru/v6_top_pics/ampresize/media/img/6/03/755735496198036.jpg'),
         ('Kia Rio', 'https://autoreview.ru/images/Article/1601/Article_160191_860_575.jpg'),
         ('Kia Sportage', 'https://upload.wikimedia.org/wikipedia/commons/1/1f/2019_Kia_Sportage_2_CRDi_ISG_S-A_1.6_Front.jpg'),
         ('Skoda Rapid', 'https://avatars.mds.yandex.net/get-verba/997355/2a0000016efea787dd46c599a439feb532c5/cattouchret'),
         ('Mitsubishi Outlander', 'https://s.auto.drom.ru/i24225/c/photos/fullsize/mitsubishi/outlander/mitsubishi_outlander_841493.jpg'),
         ('Volkswagen Tiguan', 'https://data.favorit-motors.ru/upload/iblock/0b2/0b23febd18beee323d30bac95103858d.jpg'),
         ('Kia Rio X-Line', 'https://data.favorit-motors.ru/upload/iblock/72e/72ec00adfd418c2aba336f8531b69a8e.jpg'),
         ('Volkswagen Polo', 'https://data.favorit-motors.ru/upload/iblock/033/0338af123bcd85f7c6463ec4b5da9faa.jpg')]

conn = sqlite3.connect('database.db')
c = conn.cursor()


def insert(model, color, description, img_url, cost, count): return c.execute(
    f"INSERT INTO autos (model, color, description, img_url, cost, count) VALUES('{model}', '{color}', '{description}', '{img_url}', {cost}, {count});")


[[insert(
    model,
    r.choice(сolors),
    description,
    img_url,
    r.randint(500_000, 1_000_000),
    r.randint(500,1_000)) for model, img_url in autos] for _ in range(2)]
conn.commit()
