# Generated by Django 5.2 on 2025-05-05 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_books',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_menu_items',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
