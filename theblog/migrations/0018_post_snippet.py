# Generated by Django 4.0.2 on 2024-03-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0017_post_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]