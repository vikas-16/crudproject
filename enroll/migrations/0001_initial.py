# Generated by Django 3.0.5 on 2022-06-15 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', editable=False, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('upload', models.ImageField(blank=True, upload_to='media')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.Category')),
            ],
        ),
    ]
