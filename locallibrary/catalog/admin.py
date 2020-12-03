from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)

#이 코드는 모델들을 import하고 그것들을 등록하기 위해 admin.site.register 를 호출합니다.
