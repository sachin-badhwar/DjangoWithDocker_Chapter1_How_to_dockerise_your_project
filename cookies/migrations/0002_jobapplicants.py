# Generated by Django 3.0.8 on 2020-08-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('resume', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
