from flask_restx import fields


class AuthRequestSchema():
    def __init__(self, namespace):
        self.namespace = namespace

    def signIn(self):
        return self.namespace.model('Create Token', {
            'username': fields.String(required=True),
            'password': fields.String(required=True)
        })
