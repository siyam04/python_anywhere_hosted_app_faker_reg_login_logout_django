# Generated by Django 2.1.2 on 2018-10-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('verify_email', models.EmailField(max_length=50)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
