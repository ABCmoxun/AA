from django.db import models

# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    website=models.URLField()

#创建Author模型类，
#name,姓名，age,年龄,email,邮箱
class Author(models.Model):
    names = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)

#创建Book模型类
#title,书名,publicate_date出版时间
class Book(models.Model):
    title = models.CharField(max_length=50)
    publicate_date = models.DateField()