from django.urls import path

from core.views import SearchView, ResultView

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('result/', ResultView.as_view(), name='result'),
]