# Generated by Django 5.0.3 on 2024-04-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_rename_referreddoctor_slot_referredfrom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='speciality',
            field=models.CharField(default='ENT', max_length=30),
        ),
    ]