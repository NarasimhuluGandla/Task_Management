from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('Add_task/',views.create,name='create'),
    path('delete/<int:id>',views.dele,name='delete'),
    path('history/',views.history,name='history'),
    path('update/<int:id>',views.upd,name='update'),
    path('restore/<int:id>',views.restore,name='restore'),
    path('del/<int:id>',views.dele_restore,name='del'),
    path('restoreall/',views.restore_all,name='restoreall'),
    path('deleteall/',views.deleteall,name='deleteall'),
    path('about/',views.about,name='about')
]
