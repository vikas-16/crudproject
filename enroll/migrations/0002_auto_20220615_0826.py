# Generated by Django 3.0.5 on 2022-06-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
