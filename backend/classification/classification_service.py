"""
Document Classification Service (Supervised)
Implements a Multinomial Naive Bayes classifier with TF-IDF features.
Provides training, prediction, metrics and sample document retrieval.
"""
import os
import pickle
import json
from pathlib import Path
import re
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Import real-world documents from data.py
try:
    import sys
    from pathlib import Path
    # Add parent directory to path to import data.py
    parent_dir = Path(__file__).resolve().parent.parent.parent
    if str(parent_dir) not in sys.path:
        sys.path.insert(0, str(parent_dir))
    from data import documents
    print(f"[ClassificationService] Loaded {len(documents)} real-world documents from data.py")
except ImportError:
    print("[ClassificationService] Warning: Could not import documents from data.py, using empty list")
    documents = []


class ClassificationService:
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent.parent
        self.models_dir = self.base_dir / 'models'
        self.data_dir = self.base_dir / 'data'
        self.static_dir = self.base_dir / 'static'

        self.models_dir.mkdir(exist_ok=True)
        self.data_dir.mkdir(exist_ok=True)
        self.static_dir.mkdir(exist_ok=True)

        self.vectorizer = None
        self.model = None
        self.label_classes = []

        # try to load saved artifacts
        self.load_models()

    def _preprocess(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        text = text.lower()
        tokens = re.findall(r"[a-z]+", text)
        return " ".join(tokens)

    def load_models(self):
        try:
            vec_path = self.models_dir / 'tfidf_vectorizer.pkl'
            model_path = self.models_dir / 'nb_classifier.pkl'
            if vec_path.exists() and model_path.exists():
                with open(vec_path, 'rb') as f:
                    self.vectorizer = pickle.load(f)
                with open(model_path, 'rb') as f:
                    self.model = pickle.load(f)
                if hasattr(self.model, 'classes_'):
                    self.label_classes = list(self.model.classes_)
                return True
            return False
        except Exception as e:
            print(f"[ClassificationService] Error loading models: {e}")
            return False

    def train_from_dataframe(self, df: pd.DataFrame, text_col='text', label_col='category'):
        df = df.dropna(subset=[text_col, label_col])
        df['clean_text'] = df[text_col].apply(self._preprocess)

        X = df['clean_text']
        y = df[label_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=1000, stop_words='english')
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        self.model = MultinomialNB()
        self.model.fit(X_train_vec, y_train)

        # persist
        with open(self.models_dir / 'tfidf_vectorizer.pkl', 'wb') as f:
            pickle.dump(self.vectorizer, f)
        with open(self.models_dir / 'nb_classifier.pkl', 'wb') as f:
            pickle.dump(self.model, f)

        self.label_classes = list(self.model.classes_)

        # evaluation
        y_pred = self.model.predict(X_test_vec)
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        metrics = {'accuracy': float(acc), 'report': report}
        with open(self.data_dir / 'classification_metrics.json', 'w') as f:
            json.dump(metrics, f, indent=2)

        # save classified documents for browsing
        df_out = df.copy()
        df_out['predicted_category'] = self.model.predict(self.vectorizer.transform(df_out['clean_text']))
        df_out.to_csv(self.data_dir / 'classified_documents.csv', index=False)

        return metrics

    def train(self, dataset_path: str = None):
        # dataset_path relative to base_dir/data or absolute
        try:
            if dataset_path:
                p = Path(dataset_path)
                if not p.exists():
                    p = self.data_dir / dataset_path
                df = pd.read_csv(p)
            elif documents:
                df = pd.DataFrame(documents)
            else:
                raise FileNotFoundError('No dataset provided and no embedded documents available')

            # expect columns 'text' and 'category'
            if 'text' not in df.columns or 'category' not in df.columns:
                raise ValueError('Dataset must contain "text" and "category" columns')

            return self.train_from_dataframe(df, text_col='text', label_col='category')
        except Exception as e:
            print(f"[ClassificationService] Training failed: {e}")
            return None

    def predict(self, text: str):
        if not self.model or not self.vectorizer:
            if not self.load_models():
                return {'error': 'Model not trained or loaded'}

        clean = self._preprocess(text)
        vec = self.vectorizer.transform([clean])
        pred = self.model.predict(vec)[0]
        probs = None
        try:
            probs = self.model.predict_proba(vec)[0]
            conf = float(max(probs))
        except Exception:
            conf = 1.0

        return {
            'category': pred,
            'confidence': conf,
            'probabilities': {c: float(p) for c, p in zip(self.label_classes, probs)} if probs is not None else {}
        }

    def get_metrics(self):
        try:
            p = self.data_dir / 'classification_metrics.json'
            if p.exists():
                with open(p, 'r') as f:
                    return json.load(f)
            return {}
        except Exception:
            return {}

    def get_sample_documents(self, category=None, limit=10):
        try:
            p = self.data_dir / 'classified_documents.csv'
            if not p.exists():
                return []
            df = pd.read_csv(p)
            if category:
                df = df[df['predicted_category'] == category]
            return df[['text', 'predicted_category']].head(limit).to_dict('records')
        except Exception:
            return []


# singleton
_service = None

def get_classification_service():
    global _service
    if _service is None:
        _service = ClassificationService()
    return _service
