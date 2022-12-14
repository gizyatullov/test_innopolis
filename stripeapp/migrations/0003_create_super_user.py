# Generated by Django 3.2.15 on 2022-09-10 08:52

from django.db import migrations
from django.contrib.auth import get_user_model

User = get_user_model()


def create_super_user(*args, **kwargs):
    User.objects.create_superuser(username='admin',
                                  password='admin')


class Migration(migrations.Migration):
    dependencies = [
        ('stripeapp', '0002_fill_table_item'),
    ]

    operations = [
        migrations.RunPython(create_super_user),
    ]
