# Generated by Django 4.2.7 on 2023-11-21 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vip',
            options={'ordering': ['-date_vip']},
        ),
        migrations.RenameField(
            model_name='vip',
            old_name='fecha',
            new_name='date_vip',
        ),
    ]
