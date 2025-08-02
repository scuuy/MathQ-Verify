# Extract metrics from multiple files
import json
import re
import os
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, confusion_matrix

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        y_true = []
        y_pred = []
        cnt = 0
        
        # Match "judgement_test": true or "judgement_test": false, case insensitive
        pattern = re.compile(r'judgement_test"\s*:\s*(true|false)', re.IGNORECASE)
        
        for item in data:
            response_text = item.get('response', '')
            # Ensure response_text is a string
            if not isinstance(response_text, (str, bytes)):
                response_text = str(response_text)
            
            # Extract judgement_test value from response
            match = pattern.search(response_text)
            if match:
                test_value = match.group(1).lower()  # "true" or "false"
                cnt += 1
            else:
                # Default value if not found
                test_value = "false"
            
            # Convert test results to labels: true->correct, false->wrong
            pred_label = "correct" if test_value == "true" else "wrong"
            # judgement_gt field: True->correct, False->wrong
            gt_label = "correct" if item.get('judgement_gt', False) else "wrong"
            
            y_true.append(gt_label)
            y_pred.append(pred_label)
        
        # Calculate metrics
        acc = accuracy_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred, pos_label="correct")
        precision = precision_score(y_true, y_pred, pos_label="correct")
        f1 = f1_score(y_true, y_pred, pos_label="correct")
        cm = confusion_matrix(y_true, y_pred, labels=["correct", "wrong"])
        
        print(f"File: {file_path}")
        print(f"Valid samples: {cnt}")
        print(f"Accuracy: {acc}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"F1 score: {f1}")
        print("Confusion Matrix:")
        print("            Pred:correct  Pred:wrong")
        print(f"True:correct    {cm[0]}")
        print(f"True:wrong      {cm[1]}")
        print("-" * 50)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def main():
    # Replace with your directory containing JSON result files
    directory = 'path/to/your/results/directory'
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                analyze_file(file_path)

if __name__ == "__main__":
    main()