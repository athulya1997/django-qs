# Generated by Django 3.2 on 2022-04-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_uploadimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=45)),
                ('lname', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
    ]
