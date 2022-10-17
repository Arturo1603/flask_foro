from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token

class AuthController:
    def __init__(self):
        self.model = UserModel
        self.schema = ''

    def signIn(self, data):
        try:
            print(data)
            if record := self.model.where(
                    username=data.get('username'), status=True
            ).first():
                if record.checkPassword(data.get('password')):
                    acces_token = create_access_token(
                        identity=record.id
                    )
                    return {
                        'acces_token': acces_token
                    }
                else:
                    raise Exception('Invalid password')
            raise Exception('The user does not exist')
        except Exception as e:
            return {
                "message": "Ocurrio algo",
                'error': str(e),
            }, 500
