# Generated by Django 4.1.3 on 2022-12-05 19:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owlBumsApp', '0012_alter_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.ManyToManyField(related_name='review_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
