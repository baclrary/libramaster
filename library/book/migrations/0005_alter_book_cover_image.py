# Generated by Django 4.1 on 2023-04-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, default='book_covers/assets/default.png', null=True, upload_to='book_covers/'),
        ),
    ]
