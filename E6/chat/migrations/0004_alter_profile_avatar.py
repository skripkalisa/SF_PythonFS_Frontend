# Generated by Django 4.0 on 2022-03-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.svg', upload_to='img/profile'),
        ),
    ]