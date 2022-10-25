from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class CommentaryModel(BaseModel):

    __tablename__ = 'commentary'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(120))
    image_url = Column(String(128))
    status = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id'), default=1)
    publication_id = Column(Integer, ForeignKey('publication.id'))

    users_commentary = relationship(
        'UserModel', uselist=False, back_populates='commentary_user')
    publication_commentary = relationship(
        'PublicationModel', uselist=False, back_populates='commentary_publication')
    reply_comment = relationship(
        'ReplyCommentModel', uselist=True, back_populates='replycomment_commentary')
