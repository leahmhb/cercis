# Generated by Django 3.0.5 on 2020-06-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0002_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='kennel_club',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Kennel Club'),
        ),
    ]
