# Generated by Django 3.2.4 on 2021-06-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
