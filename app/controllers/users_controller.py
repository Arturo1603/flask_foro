from app import db
from app.models.users_model import UserModel
from app.schemas.users_schema import UserResponseSchema
from app.utils.bucket import Bucket


class UsersController:
    def __init__(self):
        self.model = UserModel
        self.response = UserResponseSchema

        self.__allowed_extesions = ['jpg', 'png', 'jpeg', 'webp']
        self.bucket = Bucket('publicationforo', 'users')

    def search(self, id):
        return self.model.where(id=id).first()

    def changeInDB(self, record=None):
        if record:
            db.session.add(record)
            db.session.commit()
            return
        db.session.rollback()
        return

    def all(self, per_page, page):
        try:
            records = self.model.where(status=True).order_by('id').paginate(
                per_page=per_page, page=page
            )
            return {
                'message': 'listado de roles',
                'data': self.response(many=True).dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'perPage': records.per_page,
                    'TotalPages': records.pages,
                    'CurrentPage': records.page,
                }
            }, 200

        except Exception as e:
            return {
                "message": "Ocurrio algo",
                'error': str(e),
            }, 500

    def create(self, data):
        print(data['image_url'].__dict__)
        try:
            #  usamos el metodo create y le mandamos la data, puede ser data['name] o
            # mas practico mandar la data como **data, asi le mandas independientemente com un sprind operator
            # record = self.model.create(**data)
            # record.hashPassword()
            # self.changeInDB(record)
            if data['image_url'] != None:
                filename, stream = self.__validateExpresions(data['image_url'])
                image_url = self.bucket.uploadObject(stream, filename)
                data['image_url'] = image_url

            record = self.model.create(**data)
            record.hashPassword()
            self.changeInDB(record)
            return {
                'message': 'User created susccesfully',
                # dump serializa la data de json a string
                # # false porque devolvemos un objeto
                'data': self.response(many=False).dump(record)
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
                'message': 'Not found User'
            }, 404
        except Exception as e:
            return {
                "message": "Ocurrio algo",
                'error': str(e),
            }, 500

    def update(self, id, data):
        try:
            if record := self.search(id):
                if data['image_url']:
                    filename, stream = self.__validateExpresions(
                        data['image_url'])
                    image_url = self.bucket.uploadObject(stream, filename)
                    data['image_url'] = image_url

                record.update(**data)
                self.changeInDB(record)

                return self.response(many=False).dump(record), 200
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
                if record.status:
                    record.update(status=False)
                    self.changeInDB(record)
                return {
                    'message': f'User deshabilited with id: {id}'
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

    def __validateExpresions(self, image_url):
        filename = image_url.filename
        stream = image_url.stream
        extension = filename.split(".")[1]

        if extension not in self.__allowed_extesions:
            raise Exception('The type of archive is not allowed')

        return filename, stream
