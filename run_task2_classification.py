"""
Task 2: Document Classification - Main Entry Point
Runs training for the Naive Bayes classifier (saves models and metrics).
"""
import os
import sys
import django

# 1. Setup Django Environment (so classification service uses project paths)
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, 'backend')
sys.path.append(backend_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from classification.classification_service import get_classification_service


def main():
    print("========================================")
    print("   TASK 2: DOCUMENT CLASSIFICATION")
    print("========================================")

    service = get_classification_service()

    print("[1/1] Training classifier on real-world data from data.py...")
    res = service.train()  # Will use documents from data.py
    if res is None:
        print("[ERROR] Training failed. See logs for details.")
    else:
        print("[OK] Training completed. Metrics:")
        print(res)

    print("\n========== ROBUSTNESS TESTING ==========")
    robust_tests = [
        "movie music actor",
        "THE ECONOMY AND THE MARKET",
        "doctor hospital treatment patient health care",
        "stocks vaccine film economy",
        "new album released",
        "covid vaccination reduces risk"
    ]

    for test_text in robust_tests:
        pred = service.predict(test_text)
        print(f"Input: {test_text}")
        print(f"Prediction: {pred['category']} (Conf: {pred['confidence']:.4f})")
        print("-" * 60)

    print("\n[DONE] Task 2 Document Classification Complete")

if __name__ == '__main__':
    main()
