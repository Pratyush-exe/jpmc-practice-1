from flask import Flask
from flask_cors import CORS

from databases.models import database
from common.config import Config
from apps.health_check import HealthCheckup


def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    database.init(app)


app = create_app(Config)
app.add_url_rule(
    "/todo/v1/health-checkup", view_func=HealthCheckup.as_view("health_checkup")
)

if __name__ == "__main__":
    app.run(debug=True)
