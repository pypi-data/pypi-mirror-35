# Generated by Django 2.0.6 on 2018-07-02 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakenews', '0005_remove_source_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='source_type',
        ),
        migrations.DeleteModel(
            name='SourceType',
        ),
    ]
