# Generated by Django 4.2.7 on 2023-11-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_portfolio']},
        ),
        migrations.AddField(
            model_name='project',
            name='date_portfolio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
