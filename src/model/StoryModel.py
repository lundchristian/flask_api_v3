from ..database.db import Database

class StoryModel():
    
    def fetch_all():
        db = Database.open()
        stories = db.execute("SELECT * FROM story ORDER BY created DESC").fetchall()
        return stories

    def fetch_one(id):
        db = Database.open()
        story = db.execute("SELECT * FROM story WHERE id = ? ORDER BY created DESC", (id,)).fetchone()
        return story

    def create_one(title, description, author):
        db = Database.open()
        return_code = db.execute("INSERT INTO story (title, description, author) VALUES (?, ?, ?)", (title, description, author))
        db.commit()
        return return_code

    def update_one(id, title, description):
        db = Database.open()
        return_code = db.execute("UPDATE story SET title = ?, description = ? WHERE id = ?", (title, description, id))
        db.commit()
        return return_code

    def delete_all():
        db = Database.open()
        return_code = db.execute("DELETE FROM story")
        db.commit()
        return return_code

    def delete_one(id):
        db = Database.open()
        return_code = db.execute("DELETE FROM story WHERE id = ?", (id,))
        db.commit()
        return return_code