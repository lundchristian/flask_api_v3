from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from ..model.StoryModel import StoryModel

bp = Blueprint("story", __name__, url_prefix="/story")

@bp.route("/read", methods=["GET"])
def read():
    stories = StoryModel.fetch_all()
    return render_template("story/read.html", stories=stories)

@bp.route("/create", methods=["GET","POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        author = request.form["author"]

        if title and author and description is not None:
            StoryModel.create_one(title=title, description=description, author=author)
            return redirect(url_for("story.read"))

    return render_template("story/create.html")

@bp.route("/<int:id>/update", methods=["GET", "POST"])
def update(id):
    story = StoryModel.fetch_one(id)
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]

        if title and description is not None:
            StoryModel.update_one(id=id, title=title, description=description)
            return redirect(url_for("story.read"))

    return render_template('story/update.html', story=story)

@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    story = StoryModel.delete_one(id)
    return redirect(url_for("story.read"))