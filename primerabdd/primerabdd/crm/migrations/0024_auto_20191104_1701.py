# Generated by Django 2.2.5 on 2019-11-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_auto_20191104_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddConstraint(
            model_name='contacto',
            constraint=models.UniqueConstraint(fields=('cuenta', 'email'), name='email_contacto_unico'),
        ),
    ]
