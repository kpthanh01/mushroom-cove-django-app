from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('login/', views.Login.as_view(), name='login-page'),
    path('accounts/signup/', views.signup, name='signup'),
    path('mushrooms/', views.mushroom_index, name='mushroom-index'),
    path('mushrooms/<int:mushroom_id>/', views.mushroom_detail, name='mushroom-detail'),
    path('mushrooms/create', views.CreateMushroom.as_view(), name='mushroom-create'),
    path('mushrooms/<int:pk>/update/', views.MushroomUpdate.as_view(), name='mushroom-update'),
    path('mushrooms/<int:pk>/delete/', views.MushroomDelete.as_view(), name='mushroom-delete'),
    path('mushrooms/<int:mushroom_id>/add-tracking/', views.record_mushroom, name='add-tracking'),
]
