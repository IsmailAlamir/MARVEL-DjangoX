from django.urls import path
from .views import MarvelListView, MarvelDetailView, MarvelCreateView, MarvelUpdateView, MarvelDeleteView

urlpatterns = [
    path('marvel/', MarvelListView.as_view(), name='marvel_list'),
    path('marvel/<int:pk>/', MarvelDetailView.as_view(), name='marvel_detail'),
    path('marvel/create/', MarvelCreateView.as_view(), name='marvel_create'),
    path('marvel/<int:pk>/update/', MarvelUpdateView.as_view(), name='marvel_update'),
    path('marvel/<int:pk>/delete/', MarvelDeleteView.as_view(), name='marvel_delete'),
]