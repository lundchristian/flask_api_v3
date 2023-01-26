import os
from flask import (Blueprint, flash, g, redirect, render_template, request, url_for, send_file)
from ..model.ChapterModel import ChapterModel

bp = Blueprint("chapter", __name__, url_prefix="/story/<int:story_id>/chapter")

@bp.route("/read", methods=["GET"])
def read(story_id):
    chapters = ChapterModel.fetch_all(story_id=story_id)
    return render_template("chapter/read.html", chapters=chapters, story_id=story_id)

@bp.route("/create", methods=["GET","POST"])
def create(story_id):
    if request.method == "POST":
        title = request.form["title"]
        brief = request.form["brief"]
        if title and brief is not None:
            ChapterModel.create_one(story_id=story_id, title=title, brief=brief)
            return redirect(url_for("chapter.read", story_id=story_id))

    return render_template("chapter/create.html")

@bp.route("/generate", methods=["GET","POST"])
def generate(story_id):
    ChapterModel.generate_one(story_id=story_id)
    return redirect(url_for("chapter.read", story_id=story_id))

@bp.route("/download", methods=["GET","POST"])
def download(story_id):
    chapters = ChapterModel.fetch_all(story_id=story_id)
    content = ""
    for chapter in chapters:
        content += 'Title: ' + chapter['title'] + "\n" + 'Body: ' + chapter['body'] + "\n"
    if content is not None:
        book = open("src/static/book.txt", 'w')
        book.write(content)
        book.close()
        return send_file("static/book.txt", as_attachment=True)
    return redirect(url_for("chapter.read", story_id=story_id))

@bp.route("/<int:id>/update", methods=["GET", "POST"])
def update(id, story_id):
    chapter = ChapterModel.fetch_one(id=id)
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        brief = request.form["brief"]

        if title and body and brief is not None:
            ChapterModel.update_one(id=id, title=title, body=body, brief=brief)
            return redirect(url_for("chapter.read", story_id=story_id))

    return render_template('chapter/update.html', chapter=chapter, story_id=story_id)

@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete(id, story_id):
    ChapterModel.delete_one(id)
    return redirect(url_for("chapter.read", story_id=story_id))
