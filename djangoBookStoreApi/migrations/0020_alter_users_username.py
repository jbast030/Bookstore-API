# Generated by Django 4.2.2 on 2023-07-07 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBookStoreApi', '0019_alter_users_email_alter_users_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, default='default-username', max_length=255, null=True, unique=True),
        ),
    ]
