# Generated by Django 2.2.1 on 2019-05-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20190524_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='booker/user_avatar'),
        ),
    ]
