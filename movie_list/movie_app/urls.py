from django.contrib import admin
from django.urls import path, include
from . import views
app_name='movie_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail' ),
    path('add/',views.add_movie,name='add_movie'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete')

]

