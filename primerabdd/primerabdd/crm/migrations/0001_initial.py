# Generated by Django 2.2.5 on 2019-11-29 17:14

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampoCustomEstadoOportunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CampoCustomOrigen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CampoCustomTipoContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CampoCustomTipoCuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CampoCustomTipoOportunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=200)),
                ('apellido', models.CharField(default=None, max_length=200)),
                ('documento', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('cargo', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('ocupacion', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('direccion', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('ciudad', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('cod_postal', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('pais', models.IntegerField(blank=True, choices=[(0, 'Argentina'), (1, 'Ecuador'), (2, 'Peru'), (3, 'Venezuela'), (4, 'Mexico'), (5, 'Panama'), (6, 'Chile'), (7, 'Uruguay')], default=None, null=True)),
                ('fecha_de_nacimiento', models.DateField(blank=True, null=True, verbose_name='fecha de nacimiento')),
                ('tipo', models.IntegerField(blank=True, choices=[(0, 'General'), (1, 'Donante'), (2, 'Voluntario'), (3, 'Ambos')], default=0, null=True, verbose_name='Tipo de Contacto')),
                ('email', models.EmailField(default=None, max_length=254)),
                ('email_alternativo', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('sexo', models.IntegerField(choices=[(0, 'Masculino'), (1, 'Femenino'), (2, 'Otro')], default=2)),
                ('telefono', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('movil', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('recibir_novedades', models.BooleanField(default=False)),
                ('observaciones', models.TextField(blank=True, default=None, null=True)),
                ('es_voluntario', models.BooleanField(default=False)),
                ('turno', models.IntegerField(blank=True, choices=[(0, 'Mañana'), (1, 'Tarde')], null=True)),
                ('estado', models.IntegerField(blank=True, choices=[(0, 'Activo'), (1, 'Inactivo')], null=True)),
                ('habilidades', models.IntegerField(blank=True, choices=[(0, 'Informatica'), (1, 'Electricidad'), (2, 'Carpinteria'), (3, 'Otras')], null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.CampoCustomTipoContacto')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=200)),
                ('calle', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('numero', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('ciudad', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('cod_postal', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('pais', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('email_alternativo', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('telefono_alternativo', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('web', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('observaciones', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_alta', models.DateField(verbose_name='fecha de alta')),
                ('tyc_leido', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'organizaciones',
            },
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.IntegerField(blank=True, choices=[(0, 'Mañana'), (1, 'Tarde')], null=True)),
                ('estado', models.IntegerField(blank=True, choices=[(0, 'Activo'), (1, 'Inactivo')], null=True)),
                ('habilidades', models.IntegerField(blank=True, choices=[(0, 'Informatica'), (1, 'Electricidad'), (2, 'Carpinteria'), (3, 'Otras')], null=True)),
                ('contacto', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='Oportunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=200)),
                ('fecha', models.DateField(verbose_name='fecha de nacimiento')),
                ('monto_currency', djmoney.models.fields.CurrencyField(choices=[('XUA', 'ADB Unit of Account'), ('AFN', 'Afghani'), ('DZD', 'Algerian Dinar'), ('ARS', 'Argentine Peso'), ('AMD', 'Armenian Dram'), ('AWG', 'Aruban Guilder'), ('AUD', 'Australian Dollar'), ('AZN', 'Azerbaijanian Manat'), ('BSD', 'Bahamian Dollar'), ('BHD', 'Bahraini Dinar'), ('THB', 'Baht'), ('PAB', 'Balboa'), ('BBD', 'Barbados Dollar'), ('BYN', 'Belarussian Ruble'), ('BYR', 'Belarussian Ruble'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'), ('BTN', 'Bhutanese ngultrum'), ('VEF', 'Bolivar Fuerte'), ('BOB', 'Boliviano'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'), ('BRL', 'Brazilian Real'), ('BND', 'Brunei Dollar'), ('BGN', 'Bulgarian Lev'), ('BIF', 'Burundi Franc'), ('XOF', 'CFA Franc BCEAO'), ('XAF', 'CFA franc BEAC'), ('XPF', 'CFP Franc'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verde Escudo'), ('KYD', 'Cayman Islands Dollar'), ('CLP', 'Chilean peso'), ('XTS', 'Codes specifically reserved for testing purposes'), ('COP', 'Colombian peso'), ('KMF', 'Comoro Franc'), ('CDF', 'Congolese franc'), ('BAM', 'Convertible Marks'), ('NIO', 'Cordoba Oro'), ('CRC', 'Costa Rican Colon'), ('HRK', 'Croatian Kuna'), ('CUP', 'Cuban Peso'), ('CUC', 'Cuban convertible peso'), ('CZK', 'Czech Koruna'), ('GMD', 'Dalasi'), ('DKK', 'Danish Krone'), ('MKD', 'Denar'), ('DJF', 'Djibouti Franc'), ('STD', 'Dobra'), ('DOP', 'Dominican Peso'), ('VND', 'Dong'), ('XCD', 'East Caribbean Dollar'), ('EGP', 'Egyptian Pound'), ('SVC', 'El Salvador Colon'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('XBB', 'European Monetary Unit (E.M.U.-6)'), ('XBD', 'European Unit of Account 17(E.U.A.-17)'), ('XBC', 'European Unit of Account 9(E.U.A.-9)'), ('FKP', 'Falkland Islands Pound'), ('FJD', 'Fiji Dollar'), ('HUF', 'Forint'), ('GHS', 'Ghana Cedi'), ('GIP', 'Gibraltar Pound'), ('XAU', 'Gold'), ('XFO', 'Gold-Franc'), ('PYG', 'Guarani'), ('GNF', 'Guinea Franc'), ('GYD', 'Guyana Dollar'), ('HTG', 'Haitian gourde'), ('HKD', 'Hong Kong Dollar'), ('UAH', 'Hryvnia'), ('ISK', 'Iceland Krona'), ('INR', 'Indian Rupee'), ('IRR', 'Iranian Rial'), ('IQD', 'Iraqi Dinar'), ('IMP', 'Isle of Man Pound'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('KES', 'Kenyan Shilling'), ('PGK', 'Kina'), ('LAK', 'Kip'), ('KWD', 'Kuwaiti Dinar'), ('AOA', 'Kwanza'), ('MMK', 'Kyat'), ('GEL', 'Lari'), ('LVL', 'Latvian Lats'), ('LBP', 'Lebanese Pound'), ('ALL', 'Lek'), ('HNL', 'Lempira'), ('SLL', 'Leone'), ('LSL', 'Lesotho loti'), ('LRD', 'Liberian Dollar'), ('LYD', 'Libyan Dinar'), ('SZL', 'Lilangeni'), ('LTL', 'Lithuanian Litas'), ('MGA', 'Malagasy Ariary'), ('MWK', 'Malawian Kwacha'), ('MYR', 'Malaysian Ringgit'), ('TMM', 'Manat'), ('MUR', 'Mauritius Rupee'), ('MZN', 'Metical'), ('MXV', 'Mexican Unidad de Inversion (UDI)'), ('MXN', 'Mexican peso'), ('MDL', 'Moldovan Leu'), ('MAD', 'Moroccan Dirham'), ('BOV', 'Mvdol'), ('NGN', 'Naira'), ('ERN', 'Nakfa'), ('NAD', 'Namibian Dollar'), ('NPR', 'Nepalese Rupee'), ('ANG', 'Netherlands Antillian Guilder'), ('ILS', 'New Israeli Sheqel'), ('RON', 'New Leu'), ('TWD', 'New Taiwan Dollar'), ('NZD', 'New Zealand Dollar'), ('KPW', 'North Korean Won'), ('NOK', 'Norwegian Krone'), ('PEN', 'Nuevo Sol'), ('MRO', 'Ouguiya'), ('TOP', 'Paanga'), ('PKR', 'Pakistan Rupee'), ('XPD', 'Palladium'), ('MOP', 'Pataca'), ('PHP', 'Philippine Peso'), ('XPT', 'Platinum'), ('GBP', 'Pound Sterling'), ('BWP', 'Pula'), ('QAR', 'Qatari Rial'), ('GTQ', 'Quetzal'), ('ZAR', 'Rand'), ('OMR', 'Rial Omani'), ('KHR', 'Riel'), ('MVR', 'Rufiyaa'), ('IDR', 'Rupiah'), ('RUB', 'Russian Ruble'), ('RWF', 'Rwanda Franc'), ('XDR', 'SDR'), ('SHP', 'Saint Helena Pound'), ('SAR', 'Saudi Riyal'), ('RSD', 'Serbian Dinar'), ('SCR', 'Seychelles Rupee'), ('XAG', 'Silver'), ('SGD', 'Singapore Dollar'), ('SBD', 'Solomon Islands Dollar'), ('KGS', 'Som'), ('SOS', 'Somali Shilling'), ('TJS', 'Somoni'), ('SSP', 'South Sudanese Pound'), ('LKR', 'Sri Lanka Rupee'), ('XSU', 'Sucre'), ('SDG', 'Sudanese Pound'), ('SRD', 'Surinam Dollar'), ('SEK', 'Swedish Krona'), ('CHF', 'Swiss Franc'), ('SYP', 'Syrian Pound'), ('BDT', 'Taka'), ('WST', 'Tala'), ('TZS', 'Tanzanian Shilling'), ('KZT', 'Tenge'), ('XXX', 'The codes assigned for transactions where no currency is involved'), ('TTD', 'Trinidad and Tobago Dollar'), ('MNT', 'Tugrik'), ('TND', 'Tunisian Dinar'), ('TRY', 'Turkish Lira'), ('TMT', 'Turkmenistan New Manat'), ('TVD', 'Tuvalu dollar'), ('AED', 'UAE Dirham'), ('XFU', 'UIC-Franc'), ('USD', 'US Dollar'), ('USN', 'US Dollar (Next day)'), ('UGX', 'Uganda Shilling'), ('CLF', 'Unidad de Fomento'), ('COU', 'Unidad de Valor Real'), ('UYI', 'Uruguay Peso en Unidades Indexadas (URUIURUI)'), ('UYU', 'Uruguayan peso'), ('UZS', 'Uzbekistan Sum'), ('VUV', 'Vatu'), ('CHE', 'WIR Euro'), ('CHW', 'WIR Franc'), ('KRW', 'Won'), ('YER', 'Yemeni Rial'), ('JPY', 'Yen'), ('CNY', 'Yuan Renminbi'), ('ZMK', 'Zambian Kwacha'), ('ZMW', 'Zambian Kwacha'), ('ZWD', 'Zimbabwe Dollar A/06'), ('ZWN', 'Zimbabwe dollar A/08'), ('ZWL', 'Zimbabwe dollar A/09'), ('PLN', 'Zloty')], default='ARS', editable=False, max_length=3)),
                ('monto', djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0'), default_currency='ARS', max_digits=14)),
                ('campania', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('observaciones', models.TextField(blank=True, default=None, null=True)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Cuenta')),
                ('estado_oportunidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.CampoCustomEstadoOportunidad')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.CampoCustomTipoOportunidad')),
            ],
        ),
        migrations.CreateModel(
            name='Donante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.IntegerField(choices=[(0, 'Activo'), (1, 'De Baja'), (2, 'En Pausa'), (3, 'Completo')], default=0)),
                ('forma_de_pago', models.IntegerField(choices=[(0, 'Efectivo'), (1, 'Tarjeta de Débito'), (2, 'Tarjeta de Crédito'), (3, 'Mercado Pago'), (4, 'PayPal'), (5, 'Otro')], default=0)),
                ('frecuencia', models.IntegerField(choices=[(0, 'Mensual'), (1, 'Cada 2 Meses'), (2, 'Cada 3 Meses'), (3, 'Cada 6 Meses'), (4, 'Anual'), (5, 'Única Vez')], default=0)),
                ('monto_currency', djmoney.models.fields.CurrencyField(choices=[('XUA', 'ADB Unit of Account'), ('AFN', 'Afghani'), ('DZD', 'Algerian Dinar'), ('ARS', 'Argentine Peso'), ('AMD', 'Armenian Dram'), ('AWG', 'Aruban Guilder'), ('AUD', 'Australian Dollar'), ('AZN', 'Azerbaijanian Manat'), ('BSD', 'Bahamian Dollar'), ('BHD', 'Bahraini Dinar'), ('THB', 'Baht'), ('PAB', 'Balboa'), ('BBD', 'Barbados Dollar'), ('BYN', 'Belarussian Ruble'), ('BYR', 'Belarussian Ruble'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'), ('BTN', 'Bhutanese ngultrum'), ('VEF', 'Bolivar Fuerte'), ('BOB', 'Boliviano'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'), ('BRL', 'Brazilian Real'), ('BND', 'Brunei Dollar'), ('BGN', 'Bulgarian Lev'), ('BIF', 'Burundi Franc'), ('XOF', 'CFA Franc BCEAO'), ('XAF', 'CFA franc BEAC'), ('XPF', 'CFP Franc'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verde Escudo'), ('KYD', 'Cayman Islands Dollar'), ('CLP', 'Chilean peso'), ('XTS', 'Codes specifically reserved for testing purposes'), ('COP', 'Colombian peso'), ('KMF', 'Comoro Franc'), ('CDF', 'Congolese franc'), ('BAM', 'Convertible Marks'), ('NIO', 'Cordoba Oro'), ('CRC', 'Costa Rican Colon'), ('HRK', 'Croatian Kuna'), ('CUP', 'Cuban Peso'), ('CUC', 'Cuban convertible peso'), ('CZK', 'Czech Koruna'), ('GMD', 'Dalasi'), ('DKK', 'Danish Krone'), ('MKD', 'Denar'), ('DJF', 'Djibouti Franc'), ('STD', 'Dobra'), ('DOP', 'Dominican Peso'), ('VND', 'Dong'), ('XCD', 'East Caribbean Dollar'), ('EGP', 'Egyptian Pound'), ('SVC', 'El Salvador Colon'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('XBB', 'European Monetary Unit (E.M.U.-6)'), ('XBD', 'European Unit of Account 17(E.U.A.-17)'), ('XBC', 'European Unit of Account 9(E.U.A.-9)'), ('FKP', 'Falkland Islands Pound'), ('FJD', 'Fiji Dollar'), ('HUF', 'Forint'), ('GHS', 'Ghana Cedi'), ('GIP', 'Gibraltar Pound'), ('XAU', 'Gold'), ('XFO', 'Gold-Franc'), ('PYG', 'Guarani'), ('GNF', 'Guinea Franc'), ('GYD', 'Guyana Dollar'), ('HTG', 'Haitian gourde'), ('HKD', 'Hong Kong Dollar'), ('UAH', 'Hryvnia'), ('ISK', 'Iceland Krona'), ('INR', 'Indian Rupee'), ('IRR', 'Iranian Rial'), ('IQD', 'Iraqi Dinar'), ('IMP', 'Isle of Man Pound'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('KES', 'Kenyan Shilling'), ('PGK', 'Kina'), ('LAK', 'Kip'), ('KWD', 'Kuwaiti Dinar'), ('AOA', 'Kwanza'), ('MMK', 'Kyat'), ('GEL', 'Lari'), ('LVL', 'Latvian Lats'), ('LBP', 'Lebanese Pound'), ('ALL', 'Lek'), ('HNL', 'Lempira'), ('SLL', 'Leone'), ('LSL', 'Lesotho loti'), ('LRD', 'Liberian Dollar'), ('LYD', 'Libyan Dinar'), ('SZL', 'Lilangeni'), ('LTL', 'Lithuanian Litas'), ('MGA', 'Malagasy Ariary'), ('MWK', 'Malawian Kwacha'), ('MYR', 'Malaysian Ringgit'), ('TMM', 'Manat'), ('MUR', 'Mauritius Rupee'), ('MZN', 'Metical'), ('MXV', 'Mexican Unidad de Inversion (UDI)'), ('MXN', 'Mexican peso'), ('MDL', 'Moldovan Leu'), ('MAD', 'Moroccan Dirham'), ('BOV', 'Mvdol'), ('NGN', 'Naira'), ('ERN', 'Nakfa'), ('NAD', 'Namibian Dollar'), ('NPR', 'Nepalese Rupee'), ('ANG', 'Netherlands Antillian Guilder'), ('ILS', 'New Israeli Sheqel'), ('RON', 'New Leu'), ('TWD', 'New Taiwan Dollar'), ('NZD', 'New Zealand Dollar'), ('KPW', 'North Korean Won'), ('NOK', 'Norwegian Krone'), ('PEN', 'Nuevo Sol'), ('MRO', 'Ouguiya'), ('TOP', 'Paanga'), ('PKR', 'Pakistan Rupee'), ('XPD', 'Palladium'), ('MOP', 'Pataca'), ('PHP', 'Philippine Peso'), ('XPT', 'Platinum'), ('GBP', 'Pound Sterling'), ('BWP', 'Pula'), ('QAR', 'Qatari Rial'), ('GTQ', 'Quetzal'), ('ZAR', 'Rand'), ('OMR', 'Rial Omani'), ('KHR', 'Riel'), ('MVR', 'Rufiyaa'), ('IDR', 'Rupiah'), ('RUB', 'Russian Ruble'), ('RWF', 'Rwanda Franc'), ('XDR', 'SDR'), ('SHP', 'Saint Helena Pound'), ('SAR', 'Saudi Riyal'), ('RSD', 'Serbian Dinar'), ('SCR', 'Seychelles Rupee'), ('XAG', 'Silver'), ('SGD', 'Singapore Dollar'), ('SBD', 'Solomon Islands Dollar'), ('KGS', 'Som'), ('SOS', 'Somali Shilling'), ('TJS', 'Somoni'), ('SSP', 'South Sudanese Pound'), ('LKR', 'Sri Lanka Rupee'), ('XSU', 'Sucre'), ('SDG', 'Sudanese Pound'), ('SRD', 'Surinam Dollar'), ('SEK', 'Swedish Krona'), ('CHF', 'Swiss Franc'), ('SYP', 'Syrian Pound'), ('BDT', 'Taka'), ('WST', 'Tala'), ('TZS', 'Tanzanian Shilling'), ('KZT', 'Tenge'), ('XXX', 'The codes assigned for transactions where no currency is involved'), ('TTD', 'Trinidad and Tobago Dollar'), ('MNT', 'Tugrik'), ('TND', 'Tunisian Dinar'), ('TRY', 'Turkish Lira'), ('TMT', 'Turkmenistan New Manat'), ('TVD', 'Tuvalu dollar'), ('AED', 'UAE Dirham'), ('XFU', 'UIC-Franc'), ('USD', 'US Dollar'), ('USN', 'US Dollar (Next day)'), ('UGX', 'Uganda Shilling'), ('CLF', 'Unidad de Fomento'), ('COU', 'Unidad de Valor Real'), ('UYI', 'Uruguay Peso en Unidades Indexadas (URUIURUI)'), ('UYU', 'Uruguayan peso'), ('UZS', 'Uzbekistan Sum'), ('VUV', 'Vatu'), ('CHE', 'WIR Euro'), ('CHW', 'WIR Franc'), ('KRW', 'Won'), ('YER', 'Yemeni Rial'), ('JPY', 'Yen'), ('CNY', 'Yuan Renminbi'), ('ZMK', 'Zambian Kwacha'), ('ZMW', 'Zambian Kwacha'), ('ZWD', 'Zimbabwe Dollar A/06'), ('ZWN', 'Zimbabwe dollar A/08'), ('ZWL', 'Zimbabwe dollar A/09'), ('PLN', 'Zloty')], default='ARS', editable=False, max_length=3)),
                ('monto', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='ARS', max_digits=14)),
                ('fecha_de_compromiso', models.DateField(verbose_name='fecha de compromiso')),
                ('fecha_de_baja', models.DateField(verbose_name='fecha de baja')),
                ('motivo_de_baja', models.IntegerField(choices=[(0, 'No puede seguir pagando'), (1, 'Disconformidad'), (2, 'No quiere informar'), (3, 'Otro')], default=0)),
                ('contacto', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Contacto')),
            ],
        ),
        migrations.AddField(
            model_name='cuenta',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Organizacion'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.CampoCustomTipoCuenta'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='cuenta',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Cuenta'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='origen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.CampoCustomOrigen'),
        ),
        migrations.AddField(
            model_name='campocustomtipooportunidad',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Organizacion'),
        ),
        migrations.AddField(
            model_name='campocustomtipocuenta',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Organizacion'),
        ),
        migrations.AddField(
            model_name='campocustomtipocontacto',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Organizacion'),
        ),
        migrations.AddField(
            model_name='campocustomorigen',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Organizacion'),
        ),
        migrations.AddField(
            model_name='campocustomestadooportunidad',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Organizacion'),
        ),
        migrations.AddConstraint(
            model_name='cuenta',
            constraint=models.UniqueConstraint(fields=('organizacion', 'nombre'), name='nombre_cuenta_unica'),
        ),
        migrations.AddConstraint(
            model_name='contacto',
            constraint=models.UniqueConstraint(fields=('cuenta', 'email'), name='email_contacto_unico'),
        ),
    ]
