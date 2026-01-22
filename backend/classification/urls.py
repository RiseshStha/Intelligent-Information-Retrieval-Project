from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_document, name='predict_document'),
    path('train/', views.train_model, name='train_model'),
    path('documents/', views.get_documents, name='get_documents'),
    path('statistics/', views.get_statistics, name='get_statistics'),
    path('samples/', views.get_sample_documents, name='get_sample_documents'),
]
