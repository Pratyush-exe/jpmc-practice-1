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
                raise ResponseException(
                    message="error: 'title' not found", status_code=400
                )

            if payload.get("uuid"):
                print("'uuid' will be ignored", flush=True)

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

        except ResponseException:
            raise
        except Exception as error:
            raise ResponseException(
                message=f"error:{str(error)}",
                status_code=500,
            )
