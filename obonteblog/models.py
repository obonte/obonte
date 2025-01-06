from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categorys'

class Post(models.Model):
    title = models.CharField(max_length=550)
    flag = models.BooleanField(default=False,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(auto_now=True)
    leadimg = models.ImageField(default='leadimg.jpg')
    body = models.TextField()

    author = models.ForeignKey(User,on_delete=models.CASCADE, null =True, blank =True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.fullname
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True, blank=True)
    fullname = models.CharField(max_length=80)
    date_posted = models.DateTimeField(auto_now=True)
    body = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.fullname

    class Meta:
        ordering = ['-date_posted']

class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    replier = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(auto_now_add=True)
    body = models.TextField()


    def __str__(self):
        return f'{str(self.comment)}'

    class Meta:
       ordering = ['-date_posted']
