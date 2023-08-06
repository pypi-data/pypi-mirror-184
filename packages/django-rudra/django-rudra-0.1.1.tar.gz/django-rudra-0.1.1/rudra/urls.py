from django.urls import path
from rudra import views

urlpatterns = [
    path('models/', views.AllModels.as_view()),
    path('<str:model_name>/', views.QueryModel.as_view()),
    path('query/<str:model_name>/', views.DeepQueryModel.as_view())
]
