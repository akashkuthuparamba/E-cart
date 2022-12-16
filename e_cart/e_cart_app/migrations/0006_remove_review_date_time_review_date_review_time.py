# Generated by Django 4.1.1 on 2022-12-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_cart_app', '0005_review_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date_time',
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='review',
            name='time',
            field=models.TimeField(default=None),
        ),
    ]