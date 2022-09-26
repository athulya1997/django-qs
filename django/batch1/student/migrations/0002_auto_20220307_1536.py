# Generated by Django 3.2 on 2022-03-07 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.reg')),
            ],
        ),
    ]