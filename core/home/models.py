from accounts.models import CustomUserModel
from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.slug} - {self.updated_date}'

    def get_absolute_url(self):
        return reverse('home:detail_post', args=(self.id, self.slug))


class Comments(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='ucomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:15]}'