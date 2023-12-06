from django.urls import path
from . import views
urlpatterns = [
    path('',views.ItemListView.as_view(), name='list'),
    path('update_likes/<int:id>/<str:type>/', views.update_reactions, name='update_likes'), 
    path('update_dislikes/<int:id>/<str:type>/', views.update_reactions, name='update_dislikes'),
]
