from common.views import BaseView
from exceptions import ResponseException
from databases.models import Task, database

from flask import request


class Update(BaseView):
    def put(self, id):
        try:
            task = Task.query.filter_by(id=id).first()
            if task:
                payload = request.json
                task.title = payload.get("title", task.title)
                task.description = payload.description("description", task.description)

                database.session.commit()

                response_data = {
                    "message": "task updated",
                    "task_id": id,
                }
                status_code = 200

            else:
                response_data = {
                    "message": "task not found",
                    "task_id": id,
                }
                status_code = 404
            return self.get_response(response_data, status_code)

        except Exception as error:
            raise ResponseException(
                message={"message": "error occured", "error": str(error)},
                status_code=500,
            )
