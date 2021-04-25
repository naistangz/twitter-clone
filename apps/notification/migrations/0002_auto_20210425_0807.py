# Generated by Django 3.1.7 on 2021-04-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('message', 'Message'), ('follower', 'Follower'), ('like', 'Like'), ('mention', 'Mention')], max_length=20),
        ),
    ]
