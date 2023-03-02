from django.db import models



class posts(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
