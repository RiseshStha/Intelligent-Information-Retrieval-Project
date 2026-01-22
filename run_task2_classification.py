"""
Task 2: Document Classification
Train Naive Bayes classifier and test robustness.
"""
import os
import sys
import django

# Setup Django environment
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, 'backend')
sys.path.append(backend_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from classification.classification_service import get_classification_service


def main():
    print("=" * 40)
    print("TASK 2: DOCUMENT CLASSIFICATION")
    print("=" * 40)

    service = get_classification_service()

    # Train classifier
    print("[1/1] Training classifier on real-world data...")
    res = service.train()
    if res is None:
        print("[ERROR] Training failed. See logs for details.")
    else:
        print("[OK] Training completed. Metrics:")
        print(res)

    # Test robustness with varied inputs
    print("\n" + "=" * 40)
    print("ROBUSTNESS TESTING")
    print("=" * 40)
    
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

    print("\n[DONE] Task 2 Complete")

if __name__ == '__main__':
    main()
