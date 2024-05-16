from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return 'Post'+self.title

class Comment(models.Model):
    text = models.TextField()
    to_post = models.ForeignKey(Post, models.CASCADE)

#python manage.py makemigrations
#python manage.py migrate