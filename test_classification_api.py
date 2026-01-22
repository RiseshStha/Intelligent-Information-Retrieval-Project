"""
Test script for Task 2 Classification API
Tests all endpoints and demonstrates robustness
"""
import requests
import json

BASE_URL = 'http://localhost:8000/api/classification'

def test_predict():
    """Test document prediction endpoint"""
    print("=" * 60)
    print("TESTING PREDICTION ENDPOINT")
    print("=" * 60)
    
    test_cases = [
        "The central bank increased interest rates to control inflation",
        "The actor won an award for his latest movie",
        "Doctors warn about rising cases of flu this winter",
        "movie music actor",
        "THE ECONOMY AND THE MARKET",
        "doctor hospital treatment patient health care",
        "stocks vaccine film economy",
        "new album released",
        "covid vaccination reduces risk"
    ]
    
    for i, text in enumerate(test_cases, 1):
        try:
            response = requests.post(
                f'{BASE_URL}/predict/',
                json={'text': text},
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"\n[Test {i}] Input: {text}")
                print(f"Category: {result.get('category', 'N/A')}")
                print(f"Confidence: {result.get('confidence', 0):.4f}")
                if 'probabilities' in result:
                    print("Probabilities:")
                    for cat, prob in result['probabilities'].items():
                        print(f"  {cat}: {prob:.4f}")
            else:
                print(f"\n[Test {i}] ERROR: {response.status_code}")
                print(response.text)
        except Exception as e:
            print(f"\n[Test {i}] EXCEPTION: {e}")
    
    print("\n" + "=" * 60)

def test_statistics():
    """Test statistics endpoint"""
    print("\nTESTING STATISTICS ENDPOINT")
    print("=" * 60)
    
    try:
        response = requests.get(f'{BASE_URL}/statistics/')
        if response.status_code == 200:
            stats = response.json()
            print(f"Accuracy: {stats.get('accuracy', 'N/A')}")
            if 'report' in stats:
                print("\nClassification Report:")
                for category, metrics in stats['report'].items():
                    if isinstance(metrics, dict) and 'precision' in metrics:
                        print(f"\n{category}:")
                        print(f"  Precision: {metrics['precision']:.4f}")
                        print(f"  Recall: {metrics['recall']:.4f}")
                        print(f"  F1-Score: {metrics['f1-score']:.4f}")
                        print(f"  Support: {metrics['support']}")
        else:
            print(f"ERROR: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"EXCEPTION: {e}")
    
    print("=" * 60)

def test_samples():
    """Test sample documents endpoint"""
    print("\nTESTING SAMPLE DOCUMENTS ENDPOINT")
    print("=" * 60)
    
    categories = ['Business', 'Entertainment', 'Health']
    
    for category in categories:
        try:
            response = requests.get(f'{BASE_URL}/samples/?category={category}&limit=3')
            if response.status_code == 200:
                data = response.json()
                print(f"\n{category} Samples ({data.get('count', 0)}):")
                for i, sample in enumerate(data.get('samples', []), 1):
                    print(f"  {i}. {sample.get('text', 'N/A')[:80]}...")
            else:
                print(f"ERROR for {category}: {response.status_code}")
        except Exception as e:
            print(f"EXCEPTION for {category}: {e}")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("TASK 2: DOCUMENT CLASSIFICATION API TESTS")
    print("=" * 60)
    print("Make sure the backend server is running on http://localhost:8000")
    print("=" * 60 + "\n")
    
    test_predict()
    test_statistics()
    test_samples()
    
    print("\n[DONE] All API tests completed")
