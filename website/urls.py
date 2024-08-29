from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name="profile"),
    path('records', views.records, name="records"),
    path('financialaid', views.financialaid, name="financialaid")
]