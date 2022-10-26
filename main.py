
from app import app, db
from app.helpers import jwt
# importamos las rutas

from app import routers
from app import helpers

from app.models.base import BaseModel

BaseModel.set_session(db.session)