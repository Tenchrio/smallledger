# Generated by Django 2.2.4 on 2019-08-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SmallLedgerSite', '0005_auto_20190810_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracost',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extracosts', to='SmallLedgerSite.Item'),
        ),
    ]
