from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.roles_model import RolModel

# usamos flask_Restx nos ayuda a serializar los request


class RolesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    # Creamos los metodos
    # Metodo para la creacion
    def create(self):
        return self.namespace.model('Role Create', {

            'name': fields.String(required=True, max_length=120)
        })

    def update(self):
        return self.namespace.model('Role Update', {

            'name': fields.String(required=True, max_length=120)
        })



# Usamos marshemllow, nos ayuda a serializar lo que recibimos, response


class RolesResponseSchema(SQLAlchemyAutoSchema):

    # Clase o subclase de configuracion
    class Meta:
        model = RolModel
        ordered = True
    
    users = Nested('UserResponseSchema', exclude=['role'], many=True)
