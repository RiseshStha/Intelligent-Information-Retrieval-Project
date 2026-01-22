import json
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / 'data'
    
    # Load Metrics for classification
    try:
        with open(data_dir / 'classification_metrics.json', 'r') as f:
            metrics = json.load(f)

        print("\n\n")
        print("=" * 70)
        print("EVALUATION METRICS - DOCUMENT CLASSIFICATION")
        print("=" * 70)

        print(f"Accuracy: {metrics.get('accuracy', 0.0):.4f}")
        print("\nClassification Report:\n")
        report = metrics.get('report', {})
        if report:
            # print per-class f1 scores if available
            for label, vals in report.items():
                if isinstance(vals, dict):
                    print(f"{label}: precision={vals.get('precision',0):.4f}, recall={vals.get('recall',0):.4f}, f1={vals.get('f1-score',0):.4f}")

        print("=" * 70)

    except FileNotFoundError:
        print("Metrics file not found. Please run classification training first.")
    except Exception as e:
        print(f"Error displaying results: {e}")

if __name__ == "__main__":
    main()
