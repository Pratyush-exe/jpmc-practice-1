from flask_sqlalchemy import SQLAlchemy


database = SQLAlchemy()


class Task(database.Model):
    __tablename__ = "task"
    uuid = database.Column(database.String(36), primary_key=True)
    title = database.Column(database.String(100), unique=True, nullable=False)
    description = database.Column(database.String(500), unique=True, nullable=False)

    def json(self):
        return {"uuid": self.uuid, "title": self.title, "description": self.description}
