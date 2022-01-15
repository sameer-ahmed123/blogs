from django.db import models

# Create your models here.

class signup(models.Model):
    Realname = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    sEmail = models.EmailField(max_length=150)
    sPassword = models.CharField(max_length=250)
    class Meta:
        db_table ="Signupusers"
    def __str__(self):
        return self.Realname



class blog(models.Model):
    title =models.CharField(max_length=250)
    slug =models.SlugField()
    intro =models.TextField()
    body= models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="blog1"
        ordering =['-date_added']
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="comments"
        ordering = ['date_added']