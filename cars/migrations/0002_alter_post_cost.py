# Generated by Django 4.2.6 on 2023-10-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cost',
            field=models.TextField(),
        ),
    ]
