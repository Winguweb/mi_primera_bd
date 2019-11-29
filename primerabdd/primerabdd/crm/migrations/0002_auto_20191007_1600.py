# Generated by Django 2.2.5 on 2019-10-07 19:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='calle',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='cargo',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='ciudad',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='cod_postal',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='documento',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='email_alternativo',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='fecha_de_nacimiento',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 7, 19, 0, 41, 991742, tzinfo=utc), verbose_name='fecha de nacimiento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='movil',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='numero',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='observaciones',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='ocupacion',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='pais',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='recibir_novedades',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='calle',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='ciudad',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='cod_postal',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='email_alternativo',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='numero',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='observaciones',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='pais',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='telefono',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='telefono_alternativo',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='web',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='donante',
            name='fecha_de_baja',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 7, 19, 0, 52, 647189, tzinfo=utc), verbose_name='fecha de baja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donante',
            name='forma_de_pago',
            field=models.IntegerField(choices=[(0, 'Efectivo'), (1, 'Tarjeta de Débito'), (2, 'Tarjeta de Crédito'), (3, 'Mercado Pago'), (4, 'PayPal'), (5, 'Otro')], default=0),
        ),
        migrations.AddField(
            model_name='donante',
            name='motivo_de_baja',
            field=models.IntegerField(choices=[(0, 'No puede seguir pagando'), (1, 'Disconformidad'), (2, 'No quiere informar'), (3, 'Otro')], default=0),
        ),
        migrations.AddField(
            model_name='voluntario',
            name='dias_que_participa',
            field=models.IntegerField(blank=True, choices=[(0, 'Lunes'), (1, 'Martes'), (2, 'Miercoles'), (3, 'Jueves'), (4, 'Viernes'), (5, 'Sabado'), (6, 'Domingo')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='voluntario',
            name='habilidades',
            field=models.IntegerField(blank=True, choices=[(0, 'Informatica'), (1, 'Electricidad'), (2, 'Carpinteria'), (3, 'Otras')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Cuenta'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='nombre',
            field=models.CharField(default=None, max_length=200),
        ),
    ]