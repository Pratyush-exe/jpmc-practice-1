class Config(object):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:1234@host.docker.internal:8001/task"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
