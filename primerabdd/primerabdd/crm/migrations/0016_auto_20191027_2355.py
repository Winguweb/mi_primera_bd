# Generated by Django 2.2.5 on 2019-10-28 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0015_auto_20191027_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='documento',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]