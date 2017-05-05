from flask import render_template
from app import app, db, models

# Два декоратора route создают привязку адресов "/" и "/index" к функции
@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.all()

    data = []
    for post in posts:
        preview = post.text.split("\n")[0]
        data.append([post.id, post.title, post.date, preview])

    # Функция render_template вызывает шаблонизатор Jinja2, который
    # является частью фреймворка Flask
    return render_template("index.html", title="Блог по литературоведению", data=data)


@app.route('/post/<post_id>')
def post(post_id):
    post = models.Post.query.filter(models.Post.id == post_id).first()

    text = post.text.split("\n")
    data = [post.id, post.title, post.date, text]

    return render_template("post.html", title=data[1], data=data)
