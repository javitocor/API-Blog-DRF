from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
 
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'user: %s post id: %d' % (self.user.username, self.post.id)
