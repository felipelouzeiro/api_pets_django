# Generated by Django 4.0.5 on 2022-06-04 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adocao',
            old_name='valor',
            new_name='value',
        ),
    ]
