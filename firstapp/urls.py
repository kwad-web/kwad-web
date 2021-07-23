from django.urls import path
from .views import HomePageView, About_page

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', About_page.as_view(), name='about')
]
