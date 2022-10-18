from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token

class AuthController:
    def __init__(self):
        self.model = UserModel
        self.schema = ''

    def signIn(self, data):
        try:
            if record := self.model.where(
                    username=data.get('username'), status=True
            ).first():
                if record.checkPassword(data.get('password')):
                    acces_token = create_access_token(
                        identity=record.id
                    )
                    refresh_token= create_refresh_token(
                        identity=record.id
                    )
                    return {
                        'acces_token': acces_token,
                        'refresh_token': refresh_token
                    }
                else:
                    raise Exception('Invalid password')
            raise Exception('The user does not exist')
        except Exception as e:
            return {
                "message": "Ocurrio algo",
                'error': str(e),
            }, 500
