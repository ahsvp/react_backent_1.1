from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),  # Handles GET and POST for the item list
    path('items/<int:id>/', ItemDetailView.as_view(), name='item-detail'),  # Handles GET, PUT, PATCH for individual items
]
