from flask_sqlalchemy import SQLAlchemy


database = SQLAlchemy()


class Task(database.Model):
    table_name = "todo_list"
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), unique=True, nullable=False)
    description = database.Column(database.String(500), unique=True, nullable=False)

    def json(self):
        return {"id": self.id, "title": self.title, "description": self.description}
