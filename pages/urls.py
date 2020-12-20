from django.urls import path
from .views import HomePageView, AboutPageView, ConnectPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('connect/', ConnectPageView.as_view(), name='connect'),
    path('', HomePageView.as_view(), name='home')
]