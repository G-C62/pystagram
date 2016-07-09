from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse_lazy   #실제테이터 들어올때까지 지연해서 url을 만들어줌
# Create your models here.
class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to = '%Y/%m/%d')
    description = models.TextField(max_length = 500)    #장고에서 제한함 form validation시
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse_lazy('photos:view_photo',kwargs = {'pk':self.pk})
        return '/photos/{}/'.format(self.pk)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.description)

class Comment(models.Model):
    photo = models.ForeignKey(Photo)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}: {}'.format(self.pk, self.content)


class Like(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


@receiver(post_delete,sender=Photo)
def delete_attached_image(sender, **kwargs):        #view에서도 처리가능
    instance = kwargs.pop('instance')
    instance.image.delete(save = False)


#post_delete.connect(delete_attached_image, sender=Photo) => @receiver대신가능
