from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
   path('/', views.SignUpView.as_view(), name='main-page'),
]
