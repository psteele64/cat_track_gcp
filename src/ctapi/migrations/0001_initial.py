# Generated by Django 3.2.6 on 2022-01-02 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(choices=[('NONE', 'None'), ('GARAGE', 'Garage'), ('ADOPTCTR', 'AdoptCtr'), ('FOSTER', 'Foster')], default='NONE', max_length=8)),
                ('room_num', models.CharField(choices=[('NONE', 'None'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NONE', max_length=8)),
            ],
            options={
                'verbose_name_plural': 'cats',
            },
        ),
        migrations.CreateModel(
            name='Foster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=100)),
                ('email', models.EmailField(default='change_this_email@nowhere.com', max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'fosters',
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vet_name', models.CharField(max_length=100)),
                ('practice_name', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'vets',
            },
        ),
        migrations.CreateModel(
            name='VetVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_visited', models.DateField()),
                ('next_appt_date', models.DateField()),
                ('problem', models.TextField(blank=True, max_length=1024)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='ctapi.cat')),
                ('vet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vets', to='ctapi.vet')),
            ],
        ),
        migrations.AddField(
            model_name='vet',
            name='cats',
            field=models.ManyToManyField(related_name='vets', through='ctapi.VetVisit', to='ctapi.Cat'),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_prescribed', models.DateField()),
                ('prescription_num', models.PositiveIntegerField(unique=True)),
                ('dosage', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('instructions', models.CharField(blank=True, default='', max_length=512)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prescriptions', to='ctapi.cat')),
                ('med', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prescriptions', to='ctapi.medication')),
                ('vet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prescriptions', to='ctapi.vet')),
            ],
        ),
        migrations.AddField(
            model_name='medication',
            name='prescribed_by',
            field=models.ManyToManyField(related_name='medications', through='ctapi.Prescription', to='ctapi.Vet'),
        ),
        migrations.AddField(
            model_name='medication',
            name='prescribed_to',
            field=models.ManyToManyField(related_name='medications', through='ctapi.Prescription', to='ctapi.Cat'),
        ),
        migrations.AddField(
            model_name='cat',
            name='foster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='ctapi.foster'),
        ),
        migrations.AlterUniqueTogether(
            name='vet',
            unique_together={('vet_name', 'practice_name')},
        ),
    ]
