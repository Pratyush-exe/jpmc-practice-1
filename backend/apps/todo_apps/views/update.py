from common.views import BaseView
from exceptions import ResponseException
from databases.models import Task, database

from flask import request


class Update(BaseView):
    def put(self, uuid):
        try:
            task = Task.query.filter_by(uuid=uuid).first()
            payload = request.json
            if payload.get("uuid"):
                print("Warning: 'uuid' will be ignored")
            if task:
                task.title = payload.get("title", task.title)
                task.description = payload.get("description", task.description)

                database.session.commit()

                response_data = {
                    "message": "task updated",
                    "uuid": uuid,
                }
                status_code = 200

            else:
                response_data = {
                    "message": "task not found",
                    "uuid": uuid,
                }
                status_code = 404
            return self.get_response(response_data, status_code)

        except Exception as error:
            raise ResponseException(
                message={"message": "error occured", "error": str(error)},
                status_code=500,
            )
