# Generated by Django 4.2.3 on 2023-10-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_post_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
    ]