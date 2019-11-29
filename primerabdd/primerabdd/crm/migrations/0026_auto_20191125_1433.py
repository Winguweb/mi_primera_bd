# Generated by Django 2.2.5 on 2019-11-25 17:33

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_auto_20191125_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donante',
            name='monto',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='ARS', max_digits=14, validators=[djmoney.models.validators.MinMoneyValidator(0)]),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='monto',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0'), default_currency='ARS', max_digits=14, validators=[djmoney.models.validators.MinMoneyValidator(0)]),
        ),
    ]