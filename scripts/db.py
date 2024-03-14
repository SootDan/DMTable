import sqlite3

connector = sqlite3.connect("database/template.db")
cur = connector.cursor()

def standard_template():

    cur.execute("""CREATE TABLE IF NOT EXISTS 
    character (
    id int, race text, class text,
    gender text, pronouns text,
    CUR_HP int, MAX_HP int,
    STR int, DEX int, CON int,
    INT int, WIS int, CHA int,
    AC int, SPD int)""")
    connector.commit()
    return "Character template created."

def update_bestiary():
    cur.execute("""CREATE TABLE IF NOT EXISTS
    bestiary (
        id int, name text, hp int, ac int, spd int,
        str int, dex int, con int, int int, wis int, cha int,
        languages text, senses text, proficiency text, xp int, 
    )""")
    connector.commit()