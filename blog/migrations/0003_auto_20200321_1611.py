# Generated by Django 3.0.3 on 2020-03-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(),
        ),
    ]