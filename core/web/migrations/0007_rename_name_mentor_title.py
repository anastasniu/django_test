# Generated by Django 4.2.3 on 2023-09-30 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_mentor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='name',
            new_name='title',
        ),
    ]