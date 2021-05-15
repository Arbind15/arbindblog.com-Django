from django.db import models

from django.db import models
import sqlite3,time
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


class Blog(models.Model):
    username =models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='username',primary_key=True)
    Phone_Number=models.CharField(max_length=14,default="")
    Date=models.DateField(default=timezone.now())
    Profile_Picture=models.ImageField(default='default.png',upload_to='user_pics')
    Status=models.TextField(max_length=100,default="")
    def __str__(self):
        return f'{self.username.username} -Blog'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img1=Image.open(self.Profile_Picture.path)
        img1.thumbnail((200,200))
        img1.save(self.Profile_Picture.path)

#
class Posts(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100, default="")
    Date = models.DateField(default=timezone.now())
    Post = models.TextField(max_length=10000, default="")
    Likes = models.IntegerField(default=0)
    Remark = models.CharField(max_length=50, default="")
    def __str__(self):
        return f'{self.Title} -Post'

class Comments(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    Post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    Comment=models.TextField(max_length=100,default='')
    Date=models.DateField(default=timezone.now())
    Likes=models.IntegerField(default=0)
    def __str__(self):
        return f'{self.Post} -comment'




def database(data):
    conn=sqlite3.connect("db.sqlite3")
    conn.execute(
                '''CREATE TABLE IF NOT EXISTS main(usr text, eml text,  pass text )''')
    conn.execute("INSERT INTO main VALUES (?,?,?)",data)
    conn.commit()
    lis=conn.execute('''SELECT * FROM main''')
    for itm in lis:
        print(itm)
    conn.close()
# database(["","",""])