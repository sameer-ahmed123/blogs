# Generated by Django 4.0.1 on 2022-01-13 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_blog_blogz'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blogz',
            new_name='blog',
        ),
    ]