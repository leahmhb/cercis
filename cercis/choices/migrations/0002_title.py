# Generated by Django 3.0.5 on 2020-06-15 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('choices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('abbr', models.CharField(max_length=3, unique=True, verbose_name='Abbreviation')),
                ('sport', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sport')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active?')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'verbose_name_plural': 'Titles',
                'ordering': ['abbr', 'sport'],
                'abstract': False,
            },
        ),
    ]
