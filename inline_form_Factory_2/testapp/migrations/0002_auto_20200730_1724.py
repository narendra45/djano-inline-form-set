# Generated by Django 3.0.8 on 2020-07-30 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Profile'),
        ),
    ]
