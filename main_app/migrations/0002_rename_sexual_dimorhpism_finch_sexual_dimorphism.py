# Generated by Django 4.2 on 2023-04-12 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finch',
            old_name='sexual_dimorhpism',
            new_name='sexual_dimorphism',
        ),
    ]
