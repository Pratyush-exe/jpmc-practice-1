from flask import Flask
from flask_cors import CORS

from databases.models import database
from common.config import Config
from exceptions import ResponseException
from common.utils import jsonify_response

from apps.health_check import HealthCheckup
from apps.todo_apps.views import Create, Read, Update, Delete


def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    database.init_app(app)

    return app


app = create_app(Config)


@app.errorhandler(ResponseException)
def handle_exception(error):
    return jsonify_response(error)


app.add_url_rule("/todo/v1/create-task", view_func=Create.as_view("create"))
app.add_url_rule("/todo/v1/get-tasks", view_func=Read.as_view("read"))
app.add_url_rule("/todo/v1/update-task/<uuid>", view_func=Update.as_view("update"))
app.add_url_rule("/todo/v1/delete-task/<uuid>", view_func=Delete.as_view("delete"))
app.add_url_rule(
    "/todo/v1/health-checkup", view_func=HealthCheckup.as_view("health_checkup")
)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
