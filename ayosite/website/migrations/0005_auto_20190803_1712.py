# Generated by Django 2.2 on 2019-08-03 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20190803_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='title',
            new_name='item',
        ),
    ]
