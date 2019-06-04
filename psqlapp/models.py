from django.db import models
from django.utils.safestring import mark_safe
class Actor(models.Model):
    Name=models.CharField(max_length=50)
    address=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    age=models.PositiveIntegerField()
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.Name


    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

