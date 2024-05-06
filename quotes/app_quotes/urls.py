from django.urls import path

from . import views


app_name = 'app_quotes'

urlpatterns = [
    path("", views.hello, name='home'),
    path("/quotes", views.index, name='quotes'),
    path("/quotes/<int:page>", views.index, name='quotes_paginate'),
    path("/author/<author_name>", views.author, name='author'),
    path("/add_author", views.add_author_to_db, name='add_author'),
    path("/add_quote", views.add_quote_to_db, name='add_quote'),
]
