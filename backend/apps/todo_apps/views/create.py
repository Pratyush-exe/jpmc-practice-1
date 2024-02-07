from common.views import BaseView
from exceptions import ResponseException
from databases.models import Task, database

from flask import request


class Create(BaseView):
    def post(self):
        try:
            payload = request.json
            if not payload.get("id") or not payload.get("id"):
                raise ResponseException(message="'id' not found", status_code=400)
            new_task = Task(
                id=payload.get("id"),
                title=payload.get("title"),
                description=payload.get("description", ""),
            )
            database.session.add(new_task)
            database.session.commit()

            response_data = {
                "message": "new task created",
                "task_id": payload.get("id"),
            }
            status_code = 200
            return self.get_response(response_data, status_code)

        except Exception as error:
            raise ResponseException(
                message={"message": "error occured", "error": str(error)},
                status_code=500,
            )
