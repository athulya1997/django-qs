# Generated by Django 3.2 on 2022-03-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('des', models.TextField()),
                ('file', models.FileField(upload_to='uploads/files')),
            ],
        ),
    ]