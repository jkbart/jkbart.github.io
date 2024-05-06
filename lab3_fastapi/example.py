from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form
import sqlite3

path_to_db = "db.sqlite3"
# con = sqlite3.connect("path_to_db")
# cursor = con.cursor()


# Making a connection between sqlite3 
# database and Python Program
sqliteConnection = sqlite3.connect(path_to_db)


app = FastAPI()
# Zaimplementuj end-point listujący wszystkie tagi wraz z liczbą obrazków 
# przypisanych do danego tagu. End-point powinien być dostępny pod ścieżką /tags.
@app.get("/tags")
async def tags():
    cursor = sqliteConnection.execute('select tag_id, COUNT(*) from pictures_drawing_tags GROUP BY tag_id')
    tags = cursor.fetchall()
    data = {}
    for x in tags:
        print(x)
        data[x[0]] = x[1]
    print(data)
    return data

# Zaimplementuj end-point listujący wszystkie obrazki wraz z ich tagami. 
# End-point powinien być dostępny pod ścieżką /images.
@app.get("/images")
async def tags():
    data = {}
    cursor = sqliteConnection.execute('select id from pictures_drawing')
    drawings = cursor.fetchall()
    for x in drawings:
        # print("images", x[0])
        data[x[0]] = []
        cursor = sqliteConnection.execute('select tag_id from pictures_drawing_tags WHERE drawing_id=' + str(x[0]))
        tags = cursor.fetchall()
        for tag in tags:
            data[x[0]].append(tag[0])

    return data



# Zaimplementuj end-point listujący wszystkie obrazki przypisane do danego tagu. 
# End-point powinien być dostępny pod ścieżką /images/{tag}.
@app.get("/images/{tag}")
async def tags(tag: str):
    data = {'drawings': []}
    print('select drawing_id from pictures_drawing_tags WHERE tag_id=' + str(tag))
    cursor = sqliteConnection.execute("select drawing_id from pictures_drawing_tags WHERE tag_id=\"" + str(tag) + "\"")
    drawings = cursor.fetchall()
    for x in drawings:
        data['drawings'].append(x[0])

    return data


from typing import List
# Zaimplementuj end-point kasujący obrazki. End-point powinien być dostępny pod ścieżką /images/del. 
# Identyfikatory obrazków do skasowania powinny być przekazane w formie JSONa.
@app.post("/images/del")
async def tags(pic_ids:  List[int]):
    for id in pic_ids:
        sqliteConnection.execute('DELETE FROM pictures_drawing_author WHERE drawing_id=' + str(id))
        sqliteConnection.execute('DELETE FROM pictures_drawing WHERE id=' + str(id))
        sqliteConnection.execute('DELETE FROM pictures_drawing_tags WHERE drawing_id=' + str(id))
        sqliteConnection.execute('DELETE FROM pictures_rectangle WHERE author_id=' + str(id))
        sqliteConnection.commit()
    return 0

# curl -X POST -H "Content-Type: application/json" -d '[116]' http://localhost:8000/images/del
