from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username

    def last_10_msgs():
        return Message.objects.order_by('-date_posted').all()[:15]


# class Count(models.Model):
#     count = 10
#     def add_count(self):
#         self.count += 1
#     def sub_count(self):
#         self.count -= 1



