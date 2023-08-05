from datetime import datetime

from hadata.meta import MongoTranscriptFilter

from hadata.user import MongoUser
from hadata.answer import MongoQuestionAnswer
from mongoengine import Document, StringField, DateTimeField, ListField, ReferenceField


class MongoJobHistory(Document):
    meta = {'collection': 'job_history'}
    job_id = StringField(required=True)
    job_status = StringField(required=True)
    organization_id = StringField(required=False)  # this field is not required and should be removed from this class
    status_date_time = StringField(required=True)


class MongoJob(Document):
    meta = {'collection': 'job'}
    name = StringField(required=True)
    organization_id = StringField(required=True)
    filename = StringField(required=True)
    file_hash = StringField(required=True)
    status = StringField(required=True)
    transcript = StringField(required=False)
    user_id = StringField(required=False)
    creation_date_time = DateTimeField(required=True)
    topic = StringField(required=False)
    history = ListField(ReferenceField(MongoJobHistory), required=False, ignore_reload=True)
    questions = ListField(ReferenceField(MongoQuestionAnswer), required=False, ignore_reload=True)
    user = ReferenceField(MongoUser, required=False)
    filters = ListField(ReferenceField(MongoTranscriptFilter), required=False)

    def set_status(self, status):
        self.status = status
        job_history = MongoJobHistory()
        job_history.job_id = self.file_hash
        job_history.job_status = status
        now = datetime.now()  # current date and time
        job_history.status_date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        job_history.save()
        self.history.append(job_history)
        self.save()
