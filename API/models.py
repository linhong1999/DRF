from django.db import models

'''
    class Meta:
        # 基表  数据库不会创建
        abstract = True
'''


# 公有的一般放在 utils
class BaseModel(models.Model):
    is_delete = models.BooleanField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(BaseModel):

    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2) #小数
    img = models.ImageField(upload_to='img', default='img/default.jepg')
    publish = models.ForeignKey(to='Publish',on_delete=models.SET_NULL,db_constraint=False,null=True)
    authors = models.ManyToManyField(to='Author')

    class Meta:
        db_table = 'newbook'
        verbose_name = '新书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @property  # 也可以不写，标准写法
    def publish_name(self):
        return self.publish.name

    @property
    def author_list(self):
        return self.authors.values('name', 'age', 'authordetail__mobile').all()

class Publish(BaseModel):

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    class Meta:
        db_table = 'publish'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Author(BaseModel):

    name = models.CharField(max_length=64)
    age = models.IntegerField()

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class AuthorDetail(BaseModel):

    mobile = models.CharField(max_length=64)
    author = models.OneToOneField(to='Author',on_delete=models.SET_NULL,db_constraint=False,null=True)

    class Meta:
        db_table = 'authordetail'
        verbose_name = '作者详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s 的详情: ' % self.author.name
