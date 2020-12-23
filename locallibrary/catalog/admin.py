from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance

admin.site.register(Genre)

#이 코드는 모델들을 import하고 그것들을 등록하기 위해 admin.site.register 를 호출합니다.

#######################

# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)
# Register the admin class with the associated model

# admin.site.register(Book)
# admin.site.register(BookInstance) 
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id')


# @register 데코레이터 == admin.site.register() 동일 기능
