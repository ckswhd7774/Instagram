# Generated by Django 3.2.4 on 2021-06-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_auto_20210610_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.TextField(default=1623312589.4309812),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.TextField(default=1623312589.4309812),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='create_at',
            field=models.TextField(default=1623312589.4309812),
        ),
        migrations.AlterField(
            model_name='likearticle',
            name='create_at',
            field=models.TextField(default=1623312589.4309812),
        ),
        migrations.AlterField(
            model_name='likecomment',
            name='create_at',
            field=models.TextField(default=1623312589.4309812),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='create_at',
            field=models.TextField(default=1623312589.4309812),
        ),
    ]
