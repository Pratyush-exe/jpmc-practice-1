from common.views import BaseView
from exceptions import ResponseException
from databases.models import Task


class Read(BaseView):
    def get(self):
        try:
            tasks = Task.query.all()
            response_data = {
                "message": "success",
                "data": [task.json() for task in tasks],
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
