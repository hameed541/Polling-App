from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('poll/<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('poll/<int:poll_id>/vote/', views.vote, name='vote'),
    path('poll/<int:poll_id>/results/', views.results, name='results'),
]
