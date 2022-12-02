from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    post model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ocvliz.jpg', blank=True
    )
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return f'{self.id} {self.title}'