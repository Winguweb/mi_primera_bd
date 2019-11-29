# Generated by Django 2.2.5 on 2019-11-25 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_auto_20191104_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='campania',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='crm.CampoCustomTipoContacto'),
            preserve_default=False,
        ),
    ]
