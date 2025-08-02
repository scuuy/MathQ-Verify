import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np

# Input file path - replace with your own file path
input_file_path = "path/to/your/evaluation/data.json"

try:
    # Read input file
    with open(input_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract true_labels and pred_labels
    true_labels = []
    pred_labels = []
    for item in data:
        true_labels.append(item.get('gt'))
        pred_labels.append(item.get('test_result'))

    # Calculate metrics
    if true_labels and pred_labels:
        accuracy = accuracy_score(true_labels, pred_labels)
        precision = precision_score(true_labels, pred_labels)
        recall = recall_score(true_labels, pred_labels)
        f1 = f1_score(true_labels, pred_labels)
        # Calculate confusion matrix
        conf_matrix = confusion_matrix(true_labels, pred_labels)
    else:
        accuracy = 0
        precision = 0
        recall = 0
        f1 = 0
        conf_matrix = np.array([[0, 0], [0, 0]])

    # Output results
    print("Metrics calculated using sklearn:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-score: {f1:.4f}")
    print("\nConfusion Matrix:")
    print(conf_matrix)

except FileNotFoundError:
    print(f"Input file not found: {input_file_path}")
except Exception as e:
    print(f"Error processing file: {e}")