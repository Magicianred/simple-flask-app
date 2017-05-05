from app import db

# Класс, представляющий запись в блоге
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    date = db.Column(db.String)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Post %r>' % (self.title)
