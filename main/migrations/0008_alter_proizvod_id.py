# Generated by Django 4.1.2 on 2022-12-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_kupac_kupac_proizvodi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proizvod',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]