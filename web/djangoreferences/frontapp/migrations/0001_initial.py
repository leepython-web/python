# Generated by Django 4.1.3 on 2022-11-24 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heroRole', models.CharField(max_length=15)),
                ('heroName', models.CharField(max_length=30)),
                ('strength', models.IntegerField(default=0)),
            ],
        ),
    ]
