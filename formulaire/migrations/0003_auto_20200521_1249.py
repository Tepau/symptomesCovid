# Generated by Django 3.0.6 on 2020-05-21 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulaire', '0002_jour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.DateField(default='')),
                ('visiteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formulaire.Listing')),
            ],
        ),
        migrations.DeleteModel(
            name='Jour',
        ),
    ]
