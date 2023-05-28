from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.admin.filters import RelatedOnlyFieldListFilter


from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


class CustomManyToManyFilter(RelatedOnlyFieldListFilter):
    template = 'admin/filters/custom_m2m_filter.html'


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'middle_name', 'last_name', 'email', 'created_at', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'middle_name', 'email', 'password')
        }),
        ('Permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser')
        }),
        ('Ordered Books', {
            'fields': ('books',)
        }),
    )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'books':
            kwargs['widget'] = FilteredSelectMultiple(
                verbose_name=db_field.verbose_name,
                is_stacked=False,
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    readonly_fields = ('created_at',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'patronymic', 'surname')
    list_filter = ('name', 'surname')

    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'patronymic', 'surname')
        }),
        ('Written Books', {
            'fields': ('books',)
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count', 'display_authors')
    list_filter = ('name', 'count', 'authors__surname')

    fieldsets = (
        ('Do not change', {
            'fields': ('name', 'description', 'cover_image')
        }),
        ('May be changed', {
            'fields': ('count', )
        }),
    )

    def display_authors(self, obj):
        return ', '.join([author.get_full_name() for author in obj.authors.all()])

    display_authors.short_description = 'Authors'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'plated_end_at', 'end_at')
    list_filter = ('created_at', 'book', 'user', 'plated_end_at', 'end_at', )

    fieldsets = (
        ('Order Details', {
            'fields': ('user', 'book',)
        }),
        ('Dates', {
            'fields': ('plated_end_at', 'end_at')
        }),
    )
