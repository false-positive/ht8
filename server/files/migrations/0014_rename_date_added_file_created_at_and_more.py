# Generated by Django 4.0.3 on 2022-03-12 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0013_alter_file_name_alter_rev_date_added_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='date_added',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='date_changed',
            new_name='last_modified',
        ),
        migrations.RenameField(
            model_name='rev',
            old_name='date_added',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='rev',
            old_name='date_changed',
            new_name='last_modified',
        ),
    ]
