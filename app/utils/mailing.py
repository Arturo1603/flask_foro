from os import getenv
from app import mail
from flask_mail import Message
from flask import render_template


class Mailing:
    def __init__(self):
        self.sender = (
            'No Reply',
            getenv('MAIL_USERNAME')
        )

    def emailResetPassword(self, recipient, password):
        html = render_template('reset_password.html', password=password)
        return self.__sendEmail(
            'Reseteo de contraseña',
            [recipient],
            html
        )

    def __sendEmail(self, subject, recipients, message):
        message = Message(
            subject=subject,
            sender=self.sender,
            recipients=recipients,
            html=message
        )
        return mail.send(message)
