# Generated by Django 3.2.4 on 2021-06-08 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20210608_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='create_at',
            field=models.TextField(default=1623126537.4773738),
        ),
    ]