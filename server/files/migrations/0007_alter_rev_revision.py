# Generated by Django 4.0.3 on 2022-03-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_alter_rev_revision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rev',
            name='revision',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]