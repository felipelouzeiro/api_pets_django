# Generated by Django 4.0.5 on 2022-06-07 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0002_rename_valor_adocao_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adocao',
            old_name='value',
            new_name='donation',
        ),
    ]
