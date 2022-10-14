import restx
from app import app, db

# importamos las rutas

from app import routers


from app.models.base import BaseModel

BaseModel.set_session(db.session)