# Generated by Django 2.2.14 on 2021-06-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210605_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('C', 'Computer'), ('M', 'Mobile'), ('A', 'Accessories')], max_length=2),
        ),
    ]
