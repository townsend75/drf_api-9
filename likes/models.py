from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):

    # Likes model, related to Owner and post
    # 'owner' is a User instance and 'post' is a Post instance.
    # 'unique_together' makes sure a user can't like the same post twice.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        unique_together = [['owner', 'post']]

    def __str__(self):
        return f"{se.f.owner}, {self.post}"    
