# Generated by Django 4.1 on 2023-04-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_book_cover_image'),
        ('author', '0002_author_books_author_name_author_patronymic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='book.book', verbose_name='Written books'),
        ),
    ]
