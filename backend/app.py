from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from databases.models import task_model_factory

from apps.health_check import HealthCheckup


app = Flask(__name__)
app = CORS(app)
database = SQLAlchemy(app)

Task = task_model_factory(database)
database.create_all()

app.add_url_rule(
    "/todo/v1/health-checkup", view_func=HealthCheckup.as_view("health_checkup")
)
