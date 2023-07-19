# Generated by Django 4.1.7 on 2023-04-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Bu name alloqachon mavjud'}, max_length=255, unique=True)),
                ('slug', models.CharField(error_messages={'unique': 'Bu slug alloqachon mavjud'}, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
    ]
