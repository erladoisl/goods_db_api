from firebase_orm import models
# from django.db import models


class User(models.Model):
    email = models.TextField()
    name = models.TextField()
    uid = models.TextField()

    class Meta:
        db_table = 'users'

    def __str__(self): 
        return self.name


class Good(models.Model):
    folder_id = models.TextField()
    name = models.TextField()
    user_uid = models.ForeignKey()

    class Meta:
        db_table = 'goods'

    def __str__(self): 
        return self.name