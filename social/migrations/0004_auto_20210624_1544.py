# Generated by Django 3.2.4 on 2021-06-24 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20210624_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.TextField(default=1624517071.843189),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.TextField(default=1624517071.843189),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='create_at',
            field=models.TextField(default=1624517071.843189),
        ),
        migrations.AlterField(
            model_name='likearticle',
            name='create_at',
            field=models.TextField(default=1624517071.843189),
        ),
        migrations.AlterField(
            model_name='likecomment',
            name='create_at',
            field=models.TextField(default=1624517071.843189),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='create_at',
            field=models.TextField(default=1624517071.843189),
        ),
    ]
