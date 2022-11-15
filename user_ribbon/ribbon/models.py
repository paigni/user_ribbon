from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Картинка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


