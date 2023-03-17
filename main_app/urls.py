from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fish/', views.fish_index, name='fish_index'),
    path('fish/<int:f_id>/', views.fish_detail, name='detail'),
    path('fish/create/', views.FishCreate.as_view(), name='fish_create'),
    path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
    path('fish/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),
    path('fish/<int:f_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('fish/<int:f_id>/assoc_decoration/<int:decoration_id>/', views.assoc_decoration, name='assoc_decoration'),
    path('decorations/', views.DecorationList.as_view(), name='decorations_index'),
    path('decorations/<int:pk>/', views.DecorationDetail.as_view(), name='decorations_detail'),
    path('decorations/create/', views.DecorationCreate.as_view(), name='decorations_create'),
    path('decorations/<int:pk>/update/', views.DecorationUpdate.as_view(), name='decorations_update'),
    path('decorations/<int:pk>/delete/', views.DecorationDelete.as_view(), name='decorations_delete'),
]