# Generated by Django 3.1 on 2020-08-06 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countViewsDownload', '0002_auto_20200805_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='FJournal',
            new_name='journal',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='publicationJ',
        ),
    ]