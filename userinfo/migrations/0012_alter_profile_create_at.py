# Generated by Django 3.2.4 on 2021-06-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0011_alter_profile_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='create_at',
            field=models.TextField(default=1623656433.021137),
        ),
    ]