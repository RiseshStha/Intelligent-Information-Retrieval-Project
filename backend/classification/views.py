from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .classification_service import get_classification_service
import pandas as pd
from pathlib import Path


@api_view(['POST'])
@csrf_exempt
def predict_document(request):
    """POST /api/classification/predict/ {"text": "..."} """
    text = request.data.get('text', '')
    if not text:
        return Response({'error': 'No text provided'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        service = get_classification_service()
        result = service.predict(text)
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def train_model(request):
    """POST /api/classification/train/ Optional JSON: {"dataset_path": "relative/path.csv"} """
    dataset_path = request.data.get('dataset_path', None)
    try:
        service = get_classification_service()
        metrics = service.train(dataset_path)
        if metrics is None:
            return Response({'error': 'Training failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'status': 'ok', 'metrics': metrics}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_documents(request):
    """GET /api/classification/documents/?category=Health&limit=10"""
    category = request.query_params.get('category', None)
    limit = int(request.query_params.get('limit', 10))
    try:
        service = get_classification_service()
        samples = service.get_sample_documents(category, limit)
        return Response({'count': len(samples), 'documents': samples}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_statistics(request):
    try:
        service = get_classification_service()
        stats = service.get_metrics()
        return Response(stats, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_sample_documents(request):
    category = request.query_params.get('category', None)
    limit = int(request.query_params.get('limit', 5))
    try:
        service = get_classification_service()
        samples = service.get_sample_documents(category, limit)
        return Response({'count': len(samples), 'samples': samples}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
