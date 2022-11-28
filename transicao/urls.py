from django.urls import path
from . import views


urlpatterns = [
    path("transacoes/", views.CreateTransicaoView.as_view()),
    path("transacoes/<str:nome_loja>/", views.ListTransicaoView.as_view()),
]
