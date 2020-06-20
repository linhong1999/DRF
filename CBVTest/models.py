from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=20)
    price = models.FloatField()

    class Meta:
        db_table = 'book'
        verbose_name = '书'
        verbose_name_plural = verbose_name


# Create your models here.

class User(models.Model):
    SEX_CHOICES = [
        [0,'male'],
        [1,'female']
    ]

    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=20)
    phone = models.CharField(max_length=11,null=True,default=None)
    sex = models.IntegerField(choices=SEX_CHOICES,default=0)
    icon = models.ImageField(upload_to='icon',default='icon/default.jpeg')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.name

class Car(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='车名')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    brand = models.CharField(max_length=16, verbose_name='品牌')

    class Meta:
        db_table = 'Car'
        verbose_name = '汽车表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
