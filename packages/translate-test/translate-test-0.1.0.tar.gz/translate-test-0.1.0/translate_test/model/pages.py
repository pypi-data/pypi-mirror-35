import mongoengine

from holoread_translate.model.base_model import BaseModel


class Pages(BaseModel, mongoengine.Document):
    title = mongoengine.StringField(required=True)
    en_title = mongoengine.StringField(required=True)
    url = mongoengine.URLField(required=True, unique=True)
    source = mongoengine.StringField(required=True)

    meta = {'indexes': ['url', 'source']}

    def api_base_response(self):
        return {
            'title': self.title,
            'en_title': self.en_title,
            'url': self.url,
            'source': self.source
        }

    def api_response(self):
        return self.api_base_response()
