import json
import itertools
import multiprocessing
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score


def evaluate_combination(paths, k):
    """
    Calculate evaluation metrics for given model path combinations and threshold k.
    """
    merged_data = {}
    for path in paths:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                q_no = item["question_no"]
                if q_no not in merged_data:
                    merged_data[q_no] = {"judgement_gt": item.get("judgement_gt", False), "model_outputs": []}
                if "judgement_test" in item and item["judgement_test"] is not None:
                    merged_data[q_no]["model_outputs"].append(item["judgement_test"])

    y_true, y_pred = [], []
    tp, fp = 0, 0
    for info in merged_data.values():
        gt = "true" if info["judgement_gt"] else "false"
        true_votes = sum(1 for v in info["model_outputs"] if v)
        pred = "true" if true_votes >= k else "false"
        y_true.append(gt)
        y_pred.append(pred)
        if pred == "true":
            tp += (gt == "true")
            fp += (gt == "false")

    precision = precision_score(y_true, y_pred, pos_label="true")
    recall = recall_score(y_true, y_pred, pos_label="true")
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, pos_label="true")
    return {"paths": paths, "k": k, "accuracy": acc,
            "precision": precision, "recall": recall,
            "f1": f1, "tp": tp, "fp": fp}


def search_best_for_n_k(all_paths, max_n):
    """
    Search for optimal combinations for each n from 1..max_n and each k from 1..n.
    Returns a list containing the best result for each (n, k).
    """
    results = []
    # Iterate through n
    for n in range(1, max_n + 1):
        # Enumerate k
        for k in range(1, n + 1):
            combos = itertools.combinations(all_paths, n)
            tasks = [(combo, k) for combo in combos]
            # Parallel execution
            with multiprocessing.Pool() as pool:
                stats_list = pool.starmap(evaluate_combination, tasks)
            # Select highest precision
            best = max(stats_list, key=lambda x: x['precision'])
            best['n'] = n
            results.append(best)
    return results


if __name__ == "__main__":
    # Replace with your model result files
    all_file_paths = [
        "path/to/model1/results.json",
        "path/to/model2/results.json",
        "path/to/model3/results.json",
        "path/to/model4/results.json",
        "path/to/model5/results.json",
        "path/to/model6/results.json",
        "path/to/model7/results.json",
        "path/to/model8/results.json",
        "path/to/model9/results.json",
    ]
    max_n = 5  # Maximum number of models
    best_results = search_best_for_n_k(all_file_paths, max_n)
    # Print results
    for res in best_results:
        print(f"n={res['n']}, k={res['k']} Best combination:")
        for p in res['paths']:
            print(f"  {p}")
        print(f"  Precision: {res['precision']:.4f}, Recall: {res['recall']:.4f}, F1: {res['f1']:.4f}, "
              f"TP: {res['tp']}, FP: {res['fp']}\n")