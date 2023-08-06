import mongoengine

from holoread_translate.model.base_model import BaseModel


class RankDetail(BaseModel, mongoengine.Document):
    company = mongoengine.ObjectIdField(required=True)
    time_range = mongoengine.StringField(required=True)
    pages = mongoengine.ListField(required=True, default=[])
    news_count = mongoengine.IntField(required=False, default=0)
    financing_pages = mongoengine.ListField(required=False, default=[])
    product_pages = mongoengine.ListField(required=False, default=[])
    sentiment_pages = mongoengine.ListField(required=False, default=[])
    topic = mongoengine.ListField(required=False, default=[])
    negative_topics = mongoengine.ListField(required=False, default=[])

    meta = {'indexes': ['name', 'official_name',
                        'industry_tag', 'series_history']}

    def api_base_response(self):
        return {
            'pages': self.pages,
            'news_count': self.news_count,
            'financing_pages': self.financing_pages,
            'product_pages': self.product_pages,
            'sentiment_pages': self.sentiment_pages,
            'topic': self.topic,
            'negative_topics': self.negative_topics
        }

    def api_response(self):
        return self.api_base_response()
