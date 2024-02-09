from flask import jsonify


def jsonify_response(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
