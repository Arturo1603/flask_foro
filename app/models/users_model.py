from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class UserModel(BaseModel):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    last_name = Column(String(160))
    image_url = Column(String(128))
    email = Column(String(120), unique=True)

    username = Column(String(80), unique=True)
    password = Column(String(120), nullable=False)

    status = Column(Boolean, default=True)

    rol_id = Column(Integer, ForeignKey('roles.id'),default=1)

