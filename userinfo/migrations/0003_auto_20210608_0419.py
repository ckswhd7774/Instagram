# Generated by Django 3.2.4 on 2021-06-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20210607_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='create_at',
            field=models.TextField(default=1623125944.2515898),
        ),
    ]
