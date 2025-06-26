from django.urls import path
from tracker import views

urlpatterns = [
    path('', views.revision_view, name='revision_view'),
    path('update/<int:pk>/', views.update_problem, name='update_problem'),

]
