# Generated by Django 3.2.15 on 2022-09-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.PositiveIntegerField(verbose_name='цена')),
            ],
        ),
    ]
