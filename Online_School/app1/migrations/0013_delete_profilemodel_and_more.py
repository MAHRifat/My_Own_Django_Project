# Generated by Django 4.2.5 on 2023-10-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_coursesstoremodel_course_description_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileModel',
        ),
        migrations.AlterField(
            model_name='coursesstoremodel',
            name='course_description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='coursesstoremodel',
            name='course_name',
            field=models.CharField(max_length=30),
        ),
    ]