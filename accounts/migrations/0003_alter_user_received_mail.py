# Generated by Django 3.2.13 on 2022-12-12 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_received_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='received_mail',
            field=models.IntegerField(default=0, null=True),
        ),
    ]