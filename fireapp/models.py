from firebase_orm import models


class Good(models.Model):
    folder_id = models.TextField()
    name = models.TextField()
    user_uid = models.TextField()

    class Meta:
        db_table = 'goods'

    def __str__(self):
        return self.name


class Link(models.Model):
    good_id = models.TextField()
    name = models.TextField()
    url = models.TextField()

    class Meta:
        db_table = 'links'

    def __str__(self):
        return self.name


class Price(models.Model):
    date = models.DateField()
    good_id = models.TextField()
    link_id = models.TextField()
    price = models.FloatField()

    class Meta:
        db_table = 'prices'

    def __str__(self):
        return self.price
