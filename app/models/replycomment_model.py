from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class ReplyCommentModel(BaseModel):

    __tablename__ = 'replycomment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(120))
    image_url = Column(String(128))
    status = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id'), default=1)
    commentary_id = Column(Integer, ForeignKey('commentary.id'))

    
    replycomment_commentary = relationship('CommentaryModel',uselist=False, back_populates='reply_comment')
    users_replycomment = relationship('UserModel',uselist=False, back_populates='replycomment_user')