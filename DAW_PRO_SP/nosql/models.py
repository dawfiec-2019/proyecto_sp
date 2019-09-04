from django.db import models

from mongoengine import Document, EmbeddedDocument, fields



# Create your models here.



class laws(Document):
    name= fields.StringField()
    description = fields.StringField()
    pub_date = fields.StringField()
    summary = fields.DictField()
    details= fields.DictField()

