from common.views import BaseView
from exceptions import ResponseException
from databases.models import Task, database

from flask import request
from uuid import uuid4


class Create(BaseView):
    def post(self):
        try:
            payload = request.json
            uuid = str(uuid4())

            if not payload.get("title") or not payload.get("title"):
                raise ResponseException(message="'title' not found", status_code=400)

            if payload.get("uuid"):
                raise ResponseException(
                    message="WARNING 'uuid' will be ignored", status_code=400
                )

            new_task = Task(
                uuid=uuid,
                title=payload.get("title"),
                description=payload.get("description", ""),
            )
            database.session.add(new_task)
            database.session.commit()

            response_data = {
                "message": "new task created",
                "uuid": uuid,
            }
            status_code = 200
            return self.get_response(response_data, status_code)

        except Exception as error:
            raise ResponseException(
                message={"message": "error occured", "error": str(error)},
                status_code=500,
            )
