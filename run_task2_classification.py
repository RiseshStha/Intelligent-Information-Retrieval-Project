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
        print("\n[OK] Training completed.")
        print("-" * 65)
        print(f"{'Category':<15} {'Precision':<10} {'Recall':<10} {'F1-Score':<10} {'Support':<10}")
        print("-" * 65)
        
        report = res.get('report', {})
        for category, metrics in report.items():
            if category in ['accuracy']:
                continue
            
            # Handle macro/weighted avg
            if category in ['macro avg', 'weighted avg']:
                cat_name = category.title()
            else:
                cat_name = category

            p = metrics['precision']
            r = metrics['recall']
            f1 = metrics['f1-score']
            s = metrics['support']
            print(f"{cat_name:<15} {p:<10.4f} {r:<10.4f} {f1:<10.4f} {int(s):<10}")
        
        print("-" * 65)
        print(f"Overall Accuracy: {res['accuracy']:.4f}")
        print("-" * 65)

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
