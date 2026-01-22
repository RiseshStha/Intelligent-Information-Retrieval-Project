# Task 2: System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                    (React Frontend - Port 5173)                 │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │         ClassificationPage.jsx                            │ │
│  │  • Text input area                                        │ │
│  │  • Prediction display                                     │ │
│  │  • Confidence scores                                      │ │
│  │  • 9 test examples                                        │ │
│  │  • Probability distribution                               │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP Requests
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      REST API LAYER                             │
│                  (Django Backend - Port 8000)                   │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  classification/views.py                                  │ │
│  │  • POST /api/classification/predict/                      │ │
│  │  • GET  /api/classification/statistics/                   │ │
│  │  • GET  /api/classification/samples/                      │ │
│  │  • POST /api/classification/train/                        │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Service Calls
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CLASSIFICATION SERVICE                       │
│              (classification_service.py)                        │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  ClassificationService                                    │ │
│  │  • train(dataset_path)                                    │ │
│  │  • predict(text)                                          │ │
│  │  • get_metrics()                                          │ │
│  │  • get_sample_documents()                                 │ │
│  │  • _preprocess(text)                                      │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Uses
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      ML COMPONENTS                              │
│                                                                 │
│  ┌──────────────────────┐  ┌──────────────────────────────┐   │
│  │  TF-IDF Vectorizer   │  │  Multinomial Naïve Bayes     │   │
│  │  • ngram_range=(1,2) │  │  • sklearn.MultinomialNB     │   │
│  │  • max_features=1000 │  │  • Trained on TF-IDF vectors │   │
│  │  • stop_words='en'   │  │  • 3 classes                 │   │
│  └──────────────────────┘  └──────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Persisted to
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA LAYER                                 │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  backend/models/                                          │ │
│  │  • tfidf_vectorizer.pkl (18KB)                            │ │
│  │  • nb_classifier.pkl (24KB)                               │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  backend/data/                                            │ │
│  │  • news_dataset.csv (120 documents)                       │ │
│  │  • classification_metrics.json                            │ │
│  │  • classified_documents.csv                               │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

### Training Pipeline
```
news_dataset.csv
    │
    ├─> Load & Preprocess
    │   • Lowercase
    │   • Tokenize (regex)
    │   • Remove stopwords
    │
    ├─> Train/Test Split (80/20)
    │
    ├─> TF-IDF Vectorization
    │   • Fit on training data
    │   • Transform train & test
    │
    ├─> Train Naïve Bayes
    │   • Fit on training vectors
    │
    ├─> Evaluate
    │   • Accuracy, Precision, Recall, F1
    │
    └─> Save Artifacts
        • tfidf_vectorizer.pkl
        • nb_classifier.pkl
        • classification_metrics.json
        • classified_documents.csv
```

### Prediction Pipeline
```
User Input Text
    │
    ├─> Preprocess
    │   • Lowercase
    │   • Tokenize
    │
    ├─> TF-IDF Transform
    │   • Use saved vectorizer
    │
    ├─> Predict
    │   • Use saved classifier
    │   • Get probabilities
    │
    └─> Return Result
        • Category
        • Confidence
        • Probabilities for all classes
```

## Component Responsibilities

### Frontend (ClassificationPage.jsx)
- User input collection
- API communication
- Result visualization
- Example management

### Backend API (views.py)
- Request validation
- Service orchestration
- Response formatting
- Error handling

### Classification Service (classification_service.py)
- Model training
- Text preprocessing
- Prediction logic
- Metrics calculation
- Model persistence

### ML Models
- **TF-IDF Vectorizer**: Text → Numerical features
- **Naïve Bayes**: Features → Category prediction

### Data Storage
- **Models**: Serialized ML components
- **Datasets**: Training data & predictions
- **Metrics**: Evaluation results

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React, Axios, Tailwind CSS |
| Backend | Django, Django REST Framework |
| ML | scikit-learn, pandas, numpy |
| Preprocessing | regex, NLTK stopwords |
| Serialization | pickle, JSON |

## Performance Characteristics

- **Training Time**: ~1 second (120 documents)
- **Prediction Time**: <100ms per document
- **Model Size**: ~43KB (vectorizer + classifier)
- **Accuracy**: 100% on test set
- **API Response Time**: <200ms

## Scalability Considerations

- **Dataset**: Can handle thousands of documents
- **Features**: Limited to 1000 TF-IDF features
- **Categories**: Easily extensible to more classes
- **API**: Stateless, horizontally scalable
- **Models**: In-memory, fast predictions
