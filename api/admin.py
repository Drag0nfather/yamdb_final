from .models import Genre, Category, Title, Review, Comment
from django.contrib import admin


admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Comment)
