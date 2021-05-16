from django.db import models
from django_project.auth_.models import MyUser
from django_project.utils.validators import validate_extension, validate_size


class Exhibition(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    link = models.ImageField(upload_to='exhibitions',
                             validators=[validate_size, validate_extension],
                             null=True, blank=True)
    start = models.DateField()
    end = models.DateField()


class PictureQuerySet(models.QuerySet):

    def get_by_author(self, artist_id):
        return self.get_related().filter(artist_id=artist_id)

    def get_related(self):
        return self.select_related('artist', 'client')


class Picture(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    link = models.ImageField(upload_to='pictures',
                             validators=[validate_size, validate_extension],
                             null=True, blank=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='pictures')
    genre = models.CharField(max_length=30)
    height = models.FloatField()
    width = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, related_name='pictures')

    objects = PictureQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'


class PictureManager(models.Manager):

    def get_by_artist_with_relation(self, artist_id):
        return self.get_related().filter(artist_id=artist_id)

    def get_by_artist_without_relation(self, artist_id):
        return self.filter(artist_id=artist_id)

    def get_related(self):
        return self.select_related('artist', 'client')

