# Generated by Django 5.0.4 on 2024-04-04 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='entered_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
