# Generated by Django 4.1 on 2023-04-27 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_book_cover_image'),
        ('order', '0002_order_book_order_created_at_order_end_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='book.book', verbose_name='Ordered book'),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_at',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Returned at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='plated_end_at',
            field=models.DateTimeField(default=None, verbose_name='Should be returned until'),
        ),
    ]
