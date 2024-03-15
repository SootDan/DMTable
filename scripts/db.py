import sqlite3
from .dnd_api import fetch_bestiary

def standard_template():
    """TODO: Completely rewrite this."""
    connector = sqlite3.connect("static/database/template.db")
    cur = connector.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS 
    character (
    id int, race text, class text,
    gender text, pronouns text,
    CUR_HP int, MAX_HP int,
    STR int, DEX int, CON int,
    INT int, WIS int, CHA int,
    AC int, SPD int)""")
    connector.commit()
    cur.close()
    connector.close()


def db_bestiary(update: bool = False):
    """Creates, updates, and fetches bestiary data."""
    bestiary_db = sqlite3.connect("static/database/bestiary.db")
    cursor = bestiary_db.cursor()

    if update:
        print("Starting update process.")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bestiary (
            id INTEGER NOT NULL PRIMARY KEY, 
            name TEXT NOT NULL,
            ind TEXT NOT NULL,
            str INTEGER,
            dex INTEGER,
            con INTEGER,
            int INTEGER,
            wis INTEGER,
            cha INTEGER,
            ac INTEGER,
            hp INTEGER NOT NULL,
            size TEXT,
            spd INTEGER NOT NULL,
            xp INTEGER,
            lang TEXT,
            image TEXT
        )""")

        bestiary_db.commit()

        bestiary = fetch_bestiary()
        for monster in bestiary:
            cursor.execute("""INSERT OR REPLACE INTO bestiary (
                id, name, ind, str, dex, con, int, wis, cha, ac, hp, size, spd, xp, lang, image)
            VALUES (:id, :name, :index, :strength, :dexterity, :constitution, :intelligence, :wisdom, :charisma, :armor_class,
            :hit_points, :size, :speed, :xp, :languages, :image)""", monster)
        bestiary_db.commit()

    else:
        cursor.execute("SELECT * FROM bestiary")
        rows = cursor.fetchall()

        monster_list = []
        for row in rows:
            mob = {"name": row[1], "strength": row[3], "dexterity": row[4], "constitution": row[5], "intelligence": row[6],
            "wisdom": row[7], "charisma": row[8], "armor_class": row[9], "hit_points": row[10], "size": row[11], "speed": row[12],
            "xp": row[13], "languages": row[14], "image": row[15]}
            monster_list.append(mob)
        return monster_list
    
    cursor.close()
    bestiary_db.close()