# Generated by Django 2.2.5 on 2019-10-28 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20191027_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='nombre',
            field=models.CharField(default=None, error_messages={'unique': 'This email has already been registered.'}, max_length=200, unique=True),
        ),
    ]
