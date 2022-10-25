from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class PublicationModel(BaseModel):

    __tablename__ = 'publication'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(120))
    image_url = Column(String(128))
    status = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('UserModel', uselist=False, back_populates='publication')
    commentary_publication = relationship('CommentaryModel', uselist=True, back_populates='publication_commentary')