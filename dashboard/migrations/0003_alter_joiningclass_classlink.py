# Generated by Django 3.2.3 on 2021-05-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_noclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joiningclass',
            name='classlink',
            field=models.URLField(blank=True),
        ),
    ]