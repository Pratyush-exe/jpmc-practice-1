def task_model_factory(database):
    class TaskModel(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        title = database.Column(database.String(100), unique=True, nullable=False)
        description = database.Column(database.String(500), unique=True, nullable=False)

        def json(self):
            return {"id": self.id, "title": self.title, "description": self.description}

    return TaskModel
