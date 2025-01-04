from django.db import models


class NippoModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="タイトル")
    content = models.TextField(max_length=1000, verbose_name="内容")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title