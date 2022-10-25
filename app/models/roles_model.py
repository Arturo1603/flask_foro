from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class RolModel(BaseModel):

    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    status = Column(Boolean, default=True)
    users = relationship('UserModel', uselist=True, back_populates='role')
    
