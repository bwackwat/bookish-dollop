from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(default=now)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owner_%(class)s')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.modified = now()
        super(BaseModel, self).save(*args, **kwargs)


class Blog(BaseModel):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    style = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Post(BaseModel):
    blog = models.ForeignKey('blog', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey('blog', on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
