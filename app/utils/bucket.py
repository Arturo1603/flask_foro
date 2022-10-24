from os import getenv
from boto3 import client


class Bucket:
    def __init__(self, name, folder):
        self.name = name
        self.folder = folder
        self.region = getenv('AWS_REGION')
        self.access_key_id = getenv('AWS_ACCESS_KEY_ID')
        self.secret_access_key = getenv('AWS_SECRET_ACCESS_KEY')

        self.client = client(
            's3',
            region_name=self.region,
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key
        )

        self.__url = f'https://{self.name}.s3.{self.region}.amazonaws.com'

    def uploadObject(self, stream, filename):
        try:
            self.client.upload_fileobj(
                stream, self.name, f'{self.folder}/{filename}',
                ExtraArgs={'ACL': 'public-read'}
            )
            return f'{self.__url}/{self.folder}/{filename}'
        except Exception as e:
            raise Exception(f'Bucket error => {str(e)}') from e
