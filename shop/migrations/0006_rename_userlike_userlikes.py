# Generated by Django 3.2.25 on 2024-07-15 17:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_userlike'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserLike',
            new_name='UserLikes',
        ),
    ]
