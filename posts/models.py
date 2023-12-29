from django.db import models
from django.contrib.auth.models import User
from users.models import Profile




class Posts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_posts')

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):

        return '{} by @{}'.format(self.title, self.user.username)








