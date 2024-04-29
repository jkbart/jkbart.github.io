from django.urls import path

from . import views

app_name = "pictures"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:drawing_id>/", views.detail, name="detail"),
    path('remove_rectangle/<int:rectangle_id>/', views.remove_rectangle, name='remove_rectangle'),
    path('add_rectangle/<int:drawing_id>/', views.add_rectangle, name='add_rectangle'),
]