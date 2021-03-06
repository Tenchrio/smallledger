# Generated by Django 2.2.4 on 2019-08-13 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SmallLedgerSite', '0006_auto_20190810_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracost',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmallLedgerSite.Item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='soldprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
