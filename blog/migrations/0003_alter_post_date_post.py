# Generated by Django 4.2.7 on 2023-11-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_rename_date_post_date_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_post',
            field=models.DateField(),
        ),
    ]
