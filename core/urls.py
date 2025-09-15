from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('', home_view),
    path('students/', students_view),
    path('students/<int:student_id>/', student_details_view),
    path('students/<int:pk>/delete/', student_delete_view),
    path('students-graduate/', bitiruvchi_talabalar),
    path('authors/', authors_view),
    path('authors/<int:author_id>/', author_details_view),
    path('books/', books_view),
    path('books/<int:book_id>/', book_details_view),
    path('books/<int:pk>/delete/confirm/', book_delete_confirm_view),
    path('books/<int:pk>/delete/', book_delete_view),
]
