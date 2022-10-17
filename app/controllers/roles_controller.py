from app import db
from app.models.roles_model import RolModel
from app.schemas.roles_schema import RolesResponseSchema


class RolesController:
    def __init__(self):
        self.model = RolModel
        self.response = RolesResponseSchema

    def search(self, id):
        return self.model.where(id=id).first()

    def changeInDB(self, record=None):
        if record:
            db.session.add(record)
            db.session.commit()
            return
        db.session.rollback()
        return



    def all(self):
        try:
            records = self.model.where(status=True).order_by('id').all()
            return {
                'message': 'listado de roles',
                'data': self.response(many=True).dump(records),
            }, 200

        except Exception as e:
            return {
                "message": "Ocurrio algo",
                'error': str(e),
            }, 500

    def create(self, data):
        try:
            #  usamos el metodo create y le mandamos la data, puede ser data['name] o
            # mas practico mandar la data como **data, asi le mandas independientemente com un sprind operator
            new_record = self.model.create(**data)
            self.changeInDB(new_record)

            return {
                'message': 'El rol se creo con exito',
                # dump serializa la data de json a string
                # # false porque devolvemos un objeto
                'data': self.response(many=False).dump(new_record)
            }, 201
        except Exception as e:
            self.changeInDB()
            return {
                "message": "Ocurrio algo",
                'error': str(e),
            }, 500

    def getById(self, id):
        try:
            if record := self.search(id):
                return {
                    'data': self.response(many=False).dump(record)
                }, 200
            return {
                'message': 'Not found Rol'
            }, 404
        except Exception as e:
            return {
                "message": "Ocurrio algo",
                'error': str(e),
            }, 500

    def update(self, id, data):
        try:
            if record := self.search(id):
                record.update(**data)
                self.changeInDB(record)

                return self.response(many=False).dump(record)
            return {
                'message': 'Not Found Rol'
            }, 404
        except Exception as e:
            self.changeInDB()
            return {
                "message": "Ocurrio algo",
                "error": str(e),
            }, 500

    def delete(self, id):
        try:
            if record := self.search(id):
                if  record.status:
                    record.update(status=False)
                    self.changeInDB(record)
                return {
                    'message': f'Rol deshabilited with id: {id}'
                }, 200
            return {
                'message': 'Not Found Role'
            }, 404
        except Exception as e:
            self.changeInDB()
            return {
                "message": "Ocurrio algo",
                "error": str(e),
            }, 500
