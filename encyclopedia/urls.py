from django.urls import path

from . import views

app_name = 'ency' # Short for encylopedia
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name='entry'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    # path('create/submission', views.create_submission, name='create_submission'),
    path('edit/<str:entry>', views.edit, name='edit'),
    # path('edit/<str:entry>/sub', views.edit_submission, name='edit_submission')
    # path('wiki/<str:entry>', views.random_page, name='random_page' ),
]
