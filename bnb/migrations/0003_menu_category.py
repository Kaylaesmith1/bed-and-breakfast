# Generated by Django 3.2.18 on 2023-04-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnb', '0002_auto_20230412_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]