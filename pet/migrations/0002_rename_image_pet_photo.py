# Generated by Django 4.0.5 on 2022-06-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='image',
            new_name='photo',
        ),
    ]