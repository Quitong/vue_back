from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return 'Post'+self.title

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, models.CASCADE)
    to_post = models.ForeignKey(Post, models.CASCADE)

class Quiz(models.Model):
    title = models.CharField(max_length=200)


class Question(models.Model):
    text = models.TextField()
    to_quiz = models.ForeignKey(Quiz, models.CASCADE)


class Answer(models.Model):
    text = models.TextField()
    to_question = models.ForeignKey(Question, models.CASCADE)

#python manage.py makemigrations
#python manage.py migrate