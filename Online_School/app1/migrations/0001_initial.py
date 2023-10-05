# Generated by Django 4.2.5 on 2023-10-03 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesStoreModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('teacher_id', models.IntegerField(default=0)),
                ('course_name', models.CharField(default='Name not Given', max_length=30)),
                ('dept', models.CharField(default='None', max_length=30)),
                ('course_img', models.ImageField(default='none', upload_to='img/courses')),
                ('course_video', models.FileField(default='none', upload_to='files/courses')),
                ('course_description', models.CharField(default='', max_length=200)),
                ('first_upload', models.DateTimeField(auto_now_add=True)),
                ('last_upload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_picture', models.ImageField(upload_to='img/profile_pic')),
            ],
        ),
    ]