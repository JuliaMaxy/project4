# Generated by Django 4.2.1 on 2023-06-29 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='static/network/default-avatar.jpg', upload_to='profile_images/'),
        ),
    ]
