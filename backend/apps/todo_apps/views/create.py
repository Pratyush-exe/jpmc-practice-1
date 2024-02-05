from common.views import BaseView
from exceptions import ResponseException

from flask import request


class Create(BaseView):
    def post(self):
        try:
            payload = request.json
            if not payload.get("title"):
                raise ResponseException(message="'title' not found", status_code=400)
        except:
            pass
