# Generated by Django 4.2.2 on 2023-07-07 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBookStoreApi', '0018_alter_users_email_alter_users_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, default='default-username', max_length=255, null=True),
        ),
    ]
