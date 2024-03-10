import sqlite3

def standard_template():
    connector = sqlite3.connect("database/template.db")
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
    return "Character template created."