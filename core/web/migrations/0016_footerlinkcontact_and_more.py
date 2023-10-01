# Generated by Django 4.2.3 on 2023-10-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_footerlinkpage_rename_footerlinkpages_footerlinkblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinkContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_title', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='footerlinkblog',
            old_name='title',
            new_name='blog_title',
        ),
        migrations.RenameField(
            model_name='footerlinkpage',
            old_name='title',
            new_name='page_title',
        ),
        migrations.AlterField(
            model_name='footerlinkblog',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='footerlinkpage',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]