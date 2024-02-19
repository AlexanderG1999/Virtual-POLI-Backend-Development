from django.urls import path
from Categories import views

urlpatterns = [
    path('categories/', views.category_api),
    path('categories/<str:id>/', views.category_api),
    path('categories/id/<str:category_name>/', views.get_category_id), # Get the id of the category by the name
]