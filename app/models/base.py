# Creo dos clases, uno me activa el sqlalchemy
# el otro sus funcionamidades mixin

from app import db
from sqlalchemy_mixins import AllFeaturesMixin


class BaseModel(db.Model, AllFeaturesMixin):
    __abstract__ = True

