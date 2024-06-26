from django.urls import path
from events import views

urlpatterns = [
    path('list/', views.EventList.as_view()),
    path('<int:pk>/', views.EventDetail.as_view()),
    path('<int:pk>/register/', views.RegisterUserForEvent.as_view()),
]