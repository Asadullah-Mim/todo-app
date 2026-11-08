from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = True)
    due_date = db.Column(db.DateTime, nullable = True)
    priority = db.Column(db.String(25), default = "Medium")
    complete = db.Column(db.Boolean, default = False)
    