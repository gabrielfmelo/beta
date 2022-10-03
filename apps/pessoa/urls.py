from django.urls import path
from .views import (contacts, PessoaCreateView, PessoaListView, 
                    PessoaDetailView, PessoaUpdateView, PessoaUpdateDetailView, 
                    PessoaDeleteView)


app_name = 'pessoa'

urlpatterns= [
    path('', contacts, name='contacts'),
    path('novo/', PessoaCreateView.as_view(), name='novo'),
    path('lista/', PessoaListView.as_view(), name = 'lista'),
    path('detalhe/<int:pk>/', PessoaDetailView.as_view(), name='detalhe'),
    path('atualizar/<int:pk>/', PessoaUpdateView.as_view(), name='atualizar'),
    path('detalhe/atualizar/<int:pk>/', PessoaUpdateDetailView.as_view(), name='detalhe-atualizar'),
    path('eliminar/confirmar/<int:pk>/', PessoaDeleteView.as_view(), name='eliminar')
]