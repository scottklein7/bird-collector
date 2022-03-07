from django.urls import path, include
from main_app import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.get_bird_index, name='bird_index'),
    path('birds/<int:bird_id>/', views.get_bird_details, name='details'),
    path('birds/create/', views.BirdCreate.as_view(), name='bird_create'),
    path('birds/<int:pk>/edit/', views.BirdUpdate.as_view(), name='bird_update'),
    path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='bird_delete'),
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
