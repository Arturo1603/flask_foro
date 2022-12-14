from app import db
from app.models.commentary_model import CommentaryModel
from app.schemas.commentary_schema import CommentaryResponseSchema
from app.utils.bucket import Bucket
from flask_jwt_extended import current_user




class CommentaryController:
    def __init__(self):
        self.model = CommentaryModel
        self.response = CommentaryResponseSchema
        self.user_id = current_user['id']
        self.__allowed_extesions = ['jpg', 'png', 'jpeg', 'webp']
        self.bucket = Bucket('publicationforo', 'publications')

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
                'message': 'listado de comentarios',
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
            # record = self.model.create(**data)
            # record.hashPassword()
            # self.changeInDB(record)
            if data['image_url'] != None:
                filename, stream = self.__validateExpresions(data['image_url'])
                image_url = self.bucket.uploadObject(stream, filename)
                data['image_url'] = image_url

            data['user_id'] = self.user_id
            record = self.model.create(**data)
            self.changeInDB(record)
            return {
                'message': 'Commentary created susccesfully',
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
            if record := self.model.where(status=True, publication_id=id).first():
                return {
                    'data': self.response(many=False).dump(record)
                }, 200
            return {
                'message': 'Not found Commentary'
            }, 404
        except Exception as e:
            return {
                "message": "Ocurrio algo",
                'error': str(e),
            }, 500

    def update(self, id, data):
        try:
            if record := self.model.where(user_id=self.user_id, id=id).first():
                if data['image_url']:
                    filename, stream = self.__validateExpresions(
                        data['image_url'])
                    image_url = self.bucket.uploadObject(stream, filename)
                    data['image_url'] = image_url

                record.update(**data)
                self.changeInDB(record)

                return self.response(many=False).dump(record), 200
            return {
                'message': 'Not Found Publication'
            }, 404
        except Exception as e:
            self.changeInDB()
            return {
                "message": "Ocurrio algo",
                "error": str(e),
            }, 500

    def delete(self, id):
        try:
            if record := self.model.where(user_id=self.user_id, id=id).first():
                if record.status:
                    record.update(status=False)
                    self.changeInDB(record)
                return {
                    'message': f'Publication deshabilited with id: {id}'
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
