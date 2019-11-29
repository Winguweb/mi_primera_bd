# Generated by Django 2.2.5 on 2019-10-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20191022_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='es_voluntario',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contacto',
            name='estado',
            field=models.IntegerField(blank=True, choices=[(0, 'Activo'), (1, 'Inactivo')], null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='habilidades',
            field=models.IntegerField(blank=True, choices=[(0, 'Informatica'), (1, 'Electricidad'), (2, 'Carpinteria'), (3, 'Otras')], null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='turno',
            field=models.IntegerField(blank=True, choices=[(0, 'Mañana'), (1, 'Tarde')], null=True),
        ),
    ]