from ..database.db import Database
from .AiModel import ChatGPT
import json

class ChapterModel():
    
    def fetch_all(story_id):
        db = Database.open()
        chapters = db.execute("SELECT * FROM chapter WHERE story_id = ? ORDER BY id", (story_id,)).fetchall()
        return chapters

    def fetch_one(id):
        db = Database.open()
        chapter = db.execute("SELECT * FROM chapter WHERE id = ?", (id,)).fetchone()
        return chapter

    def create_one(story_id, title, brief):
        db = Database.open()
        return_code = db.execute("INSERT INTO chapter (story_id, title, body, brief) VALUES (?, ?, ?, ?)", (story_id, title, brief, brief))
        db.commit()
        return return_code

    def generate_one(story_id):
        stories = ChapterModel.fetch_all(story_id=story_id)
        book_summary = "BOOK START: {"
        for story in stories:
            book_summary += "\"" + str(story['id']) + "\":\"" + story['brief'] + "\","
        book_summary += "} :BOOK END"
        with open('src/static/prompt.txt', 'r') as file:
            instruction = file.read()
        prompt = book_summary + " " + instruction
        response = ChatGPT.get_response(prompt=prompt)
        response = response.replace("\n", " ")
        response_dict = json.loads(response)
        db = Database.open()
        return_code = db.execute("INSERT INTO chapter (story_id, title, body, brief) VALUES (?, ?, ?, ?)", (story_id, response_dict['title'], response_dict['body'], response_dict['brief']))
        db.commit()
        return return_code

    def update_one(id, title, body, brief):
        db = Database.open()
        return_code = db.execute("UPDATE chapter SET title = ?, body = ?, brief = ? WHERE id = ?", (title, body, brief, id))
        db.commit()
        return return_code

    def delete_all(story_id):
        db = Database.open()
        return_code = db.execute("DELETE FROM chapter WHERE story_id = ?", (story_id,))
        db.commit()
        return return_code

    def delete_one(id):
        db = Database.open()
        return_code = db.execute("DELETE FROM chapter WHERE id = ?", (id,))
        db.commit()
        return return_code