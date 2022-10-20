from app import jwt
from app.models import users_model
from app.schemas.users_schema import UserResponseSchema


@jwt.user_identity_loader
def user_identity_lookup(user_id):
    return user_id or None


@jwt.user_lookup_loader
def user_lookup_callback(header, data):
    model = users_model.UserModel
    identity = data['sub']
    record = model.where(id=identity).first()
    response = UserResponseSchema(many=False)
    return response.dump(record) or None

