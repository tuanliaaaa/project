# Generated by Django 4.0.2 on 2022-02-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_transaction_quatily'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='quatily',
            field=models.IntegerField(null=True),
        ),
    ]