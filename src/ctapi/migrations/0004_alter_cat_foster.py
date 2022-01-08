# Generated by Django 3.2.6 on 2022-01-08 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctapi', '0003_alter_cat_foster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='foster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='ctapi.foster'),
        ),
    ]
