from django.db.models import Model, CharField
from django_resized import ResizedImageField


class ProductModel(Model):
    image = ResizedImageField(size=[400, 150], crop=['middle', 'center'], upload_to='user/images',
                              default='user/default_user.jpeg')
    title = CharField(max_length=255)
    date = CharField(max_length=255)

    def __str__(self):
        return self.title
