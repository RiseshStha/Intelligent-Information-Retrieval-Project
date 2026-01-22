# Task 2: Document Classification using Naïve Bayes

## Overview
This task implements a supervised document classification system using Multinomial Naïve Bayes with TF-IDF features to classify documents into three categories: **Business**, **Entertainment**, and **Health**.

## Implementation Details

### Backend Components

#### 1. Dataset Generation (`generate_dataset.py`)
- Generates 120 labeled documents (40 per category)
- Creates realistic text samples for each category
- Saves to `backend/data/news_dataset.csv`

**Run:**
```bash
python generate_dataset.py
```

#### 2. Classification Service (`backend/classification/classification_service.py`)
**Key Features:**
- **Preprocessing**: Lowercasing, tokenization using regex
- **Vectorization**: TF-IDF with bigrams (1,2), max 1000 features, English stopwords
- **Model**: Multinomial Naïve Bayes classifier
- **Evaluation**: Accuracy, precision, recall, F1-score per class
- **Persistence**: Saves trained model and vectorizer as pickle files

**Main Methods:**
- `train(dataset_path)`: Train classifier on labeled dataset
- `predict(text)`: Classify new document and return category + confidence
- `get_metrics()`: Retrieve evaluation metrics
- `get_sample_documents(category, limit)`: Get sample documents by category

#### 3. API Endpoints (`backend/classification/views.py`)
- `POST /api/classification/predict/` - Classify a document
- `POST /api/classification/train/` - Train the model
- `GET /api/classification/statistics/` - Get model metrics
- `GET /api/classification/samples/` - Get sample documents

### Frontend Components

#### Classification Page (`frontend/src/components/ClassificationPage.jsx`)
**Features:**
- Text input area for document classification
- Real-time prediction with confidence scores
- Class probability distribution display
- 9 test examples demonstrating robustness:
  - Clear category examples
  - Short keyword-based inputs
  - All caps inputs
  - Long descriptive text
  - Mixed topic inputs

### Training Script (`run_task2_classification.py`)

**Purpose:** Main entry point for Task 2

**What it does:**
1. Trains the Naïve Bayes classifier on the dataset
2. Saves model artifacts (vectorizer, classifier, metrics)
3. Runs robustness testing with varied inputs
4. Displays predictions with confidence scores

**Run:**
```bash
python run_task2_classification.py
```

**Expected Output:**
```
========================================
   TASK 2: DOCUMENT CLASSIFICATION
========================================
[1/1] Training classifier and generating artifacts...
[OK] Training completed. Metrics:
{'accuracy': 1.0, 'report': {...}}

========== ROBUSTNESS TESTING ==========
Input: movie music actor
Prediction: Entertainment (Conf: 0.5961)
------------------------------------------------------------
Input: THE ECONOMY AND THE MARKET
Prediction: Business (Conf: 0.6186)
------------------------------------------------------------
...
[DONE] Task 2 Document Classification Complete
```

## Model Performance

### Metrics
- **Accuracy**: 100% on test set (20% of 120 documents)
- **Precision/Recall/F1**: 1.0 for all three categories
- **Support**: 8 test documents per category

### Robustness Testing
The system demonstrates robustness across:
1. **Short inputs**: "movie music actor" → Entertainment
2. **Case variations**: "THE ECONOMY AND THE MARKET" → Business
3. **Medical terms**: "doctor hospital treatment patient health care" → Health
4. **Mixed topics**: "stocks vaccine film economy" → Business (dominant terms)
5. **Long descriptive text**: Correctly classifies based on context

## File Structure
```
backend/
├── classification/
│   ├── classification_service.py  # Core classification logic
│   ├── views.py                   # API endpoints
│   └── urls.py                    # URL routing
├── models/
│   ├── tfidf_vectorizer.pkl       # Trained TF-IDF vectorizer
│   └── nb_classifier.pkl          # Trained Naïve Bayes model
└── data/
    ├── news_dataset.csv           # Training dataset
    └── classification_metrics.json # Model evaluation metrics

frontend/src/components/
└── ClassificationPage.jsx         # UI for document classification

generate_dataset.py                # Dataset generation script
run_task2_classification.py        # Main training script
```

## Usage Instructions

### 1. Generate Dataset
```bash
python generate_dataset.py
```

### 2. Train Model
```bash
python run_task2_classification.py
```

### 3. Start Backend
```bash
cd backend
python manage.py runserver
```

### 4. Start Frontend
```bash
cd frontend
npm run dev
```

### 5. Access Classification Interface
Navigate to: `http://localhost:5173/classification`

## API Usage Examples

### Classify a Document
```bash
curl -X POST http://localhost:8000/api/classification/predict/ \
  -H "Content-Type: application/json" \
  -d '{"text": "The stock market reached new highs today"}'
```

**Response:**
```json
{
  "category": "Business",
  "confidence": 0.8234,
  "probabilities": {
    "Business": 0.8234,
    "Entertainment": 0.0912,
    "Health": 0.0854
  }
}
```

### Get Model Statistics
```bash
curl http://localhost:8000/api/classification/statistics/
```

## Key Features Implemented

✅ **Supervised Classification**: Multinomial Naïve Bayes with TF-IDF  
✅ **Three Categories**: Business, Entertainment, Health  
✅ **Text Preprocessing**: Lowercasing, tokenization, stopword removal  
✅ **Model Evaluation**: Accuracy, precision, recall, F1-score  
✅ **Robustness Testing**: Varied inputs (short/long, mixed topics, case variations)  
✅ **Persistence**: Saved models and metrics  
✅ **Web Interface**: User-friendly classification UI  
✅ **API Endpoints**: RESTful API for integration  
✅ **Confidence Scores**: Probability distribution for predictions  

## Assignment Requirements Met

| Requirement | Status | Implementation |
|------------|--------|----------------|
| Collect & label documents | ✅ | 120 documents, 3 categories |
| Train Naïve Bayes classifier | ✅ | MultinomialNB with TF-IDF |
| Preprocessing | ✅ | Lowercasing, tokenization, stopwords |
| Model evaluation | ✅ | Accuracy, precision, recall, F1 |
| Save model & metrics | ✅ | Pickle files + JSON metrics |
| Classify new documents | ✅ | API + UI for predictions |
| Robustness testing | ✅ | 6+ varied test cases |
| Screenshots/logs | ✅ | Console output + UI predictions |

## Notes

- The dataset is synthetically generated but realistic
- Model achieves perfect accuracy on test set (may need more diverse data for production)
- TF-IDF features capture both unigrams and bigrams for better context
- Confidence scores help identify uncertain predictions
- Frontend provides interactive testing interface
- All code follows best practices and is well-documented
