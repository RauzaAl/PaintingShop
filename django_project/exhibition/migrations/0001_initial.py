# Generated by Django 3.2.3 on 2021-05-15 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_project.utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('link', models.ImageField(blank=True, null=True, upload_to='exhibitions', validators=[django_project.utils.validators.validate_size, django_project.utils.validators.validate_extension])),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('link', models.ImageField(blank=True, null=True, upload_to='pictures', validators=[django_project.utils.validators.validate_size, django_project.utils.validators.validate_extension])),
                ('genre', models.CharField(max_length=30)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to=settings.AUTH_USER_MODEL)),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='exhibition.exhibition')),
            ],
            options={
                'verbose_name': 'Картина',
                'verbose_name_plural': 'Картины',
            },
        ),
    ]
