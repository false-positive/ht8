# Generated by Django 4.0.3 on 2022-03-12 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0010_file_date_added_file_date_changed_rev_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]