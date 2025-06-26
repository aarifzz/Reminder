# from django.urls import path
# from tracker import views


# urlpatterns = [
#     path('', views.revision_view, name='revision_view'),
#     path('update/<int:pk>/', views.update_problem, name='update_problem'),
#     path('check-reminders/', views.check_reminders_view, name='check_reminders'),
#     path('edit/<int:pk>/', views.edit_problem, name='edit_problem'),
#     path('delete/<int:pk>/', views.delete_problem, name='delete_problem'),


# ]
from django.urls import path
from tracker import views

urlpatterns = [
    path('', views.revision_view, name='revision_view'),
    path('check-reminders/', views.check_reminders_view, name='check_reminders'),
]
