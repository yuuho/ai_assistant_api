
from auth.auth_api import db_api, auth_api
from auth.auth_common import models
from auth.auth_common.session import engine


def database_initialize():
    models.Base.metadata.create_all(bind=engine)


db_api = db_api
auth_api = auth_api
