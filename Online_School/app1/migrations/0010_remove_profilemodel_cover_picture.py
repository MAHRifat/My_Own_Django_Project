# Generated by Django 4.2.5 on 2023-10-05 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_remove_profilemodel_profile_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='cover_picture',
        ),
    ]
