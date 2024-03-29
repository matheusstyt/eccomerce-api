# Generated by Django 5.0.1 on 2024-01-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='description',
            field=models.TextField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='slug',
            field=models.CharField(default='', max_length=100),
        ),
    ]
