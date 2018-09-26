from django.db import models

# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    website=models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        db_table='publisher'
        verbose_name='出版社'
        verbose_name_plural=verbose_name

#创建Author模型类，
#name,姓名，age,年龄,email,邮箱
class Author(models.Model):
    names = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)
    #增加一个状态列，来表示用户是启用的还是禁用的，默认为True表示启用
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.names

    # 声明内部类，来定义当前类在管理页面中的展现形式
    class Meta:
            # 1.修改当前表名为 author
            db_table='author'
            # 2.修改实体类在后台管理页中的名称(单数)
            verbose_name='作者'
            # 3.修改实体类在后台管理页中的名称(复数)
            verbose_name_plural = verbose_name
            # 4.首先按照年龄降序排序，其次按照ＩＤ升序排序
            ordering = ['-age','id']

#创建Book模型类
#title,书名,publicate_date出版时间
class Book(models.Model):
    title = models.CharField(max_length=50,verbose_name='书名')
    publicate_date = models.DateField(verbose_name='出版时间')

    def __str__(self):
        return self.title

    class Meta:
        db_table='book'
        verbose_name='书籍'
        verbose_name_plural=verbose_name
        ordering=['-publicate_date']


class Wife(models.Model):
    names = models.CharField(max_length=30)
    age = models.IntegerField()
    # 增加一对一的引用，引用自Author实体
    author = models.OneToOneField(Author,null=True)

    def __str__(self):
        return self.names

    class Meta:
            db_table='wife'
            verbose_name='夫人'
            verbose_name_plural = verbose_name
