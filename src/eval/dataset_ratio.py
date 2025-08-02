import json
import matplotlib.pyplot as plt
import os

def analyze_error_distribution(file_path, save_dir="results"):
    """Analyze the distribution of error types in the dataset"""
    # Read JSON file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Initialize counters
    total_questions = len(data)
    error_types = {
        "question_format_error": 0,
        "level_0_check_error": 0,
        "min_Pi_check_error": 0,
        "contradiction_check_error": 0,
        "condition_complete_check_error": 0,
        "correct": 0
    }

    # Count each error type and correct questions
    for item in data:
        is_correct = True
        if item["question_format"] is False:
            error_types["question_format_error"] += 1
            is_correct = False
        elif item["level_0_check"] is False:
            error_types["level_0_check_error"] += 1
            is_correct = False
        elif item["min_Pi_check"] is False:
            error_types["min_Pi_check_error"] += 1
            is_correct = False
        elif item["contradiction_check"] is False:
            error_types["contradiction_check_error"] += 1
            is_correct = False
        elif item["condition_complete_check"] is False:
            error_types["condition_complete_check_error"] += 1
            is_correct = False
        
        if is_correct:
            error_types["correct"] += 1

    # Calculate percentages
    percentages = {key: (value / total_questions) * 100 for key, value in error_types.items()}

    # Print statistics
    print("Error Type and Correct Question Statistics:")
    for key in error_types:
        count = error_types[key]
        percentage = percentages[key]
        print(f"{key.ljust(30)} Count: {count:4d} | Percentage: {percentage:.2f}%")

    # Create pie chart
    labels = list(error_types.keys())
    sizes = list(error_types.values())
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=140)
    plt.axis('equal')  # Ensure pie is circular
    plt.title('Distribution of Error Types and Correct Questions')

    # Ensure save directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Save image
    save_path = os.path.join(save_dir, 'error_distribution.png')
    plt.savefig(save_path)
    print(f"Correct questions: {error_types['correct']}")
    print(f"Error questions: {total_questions - error_types['correct']}")
    
    # Display image
    plt.show()
    
    return error_types


if __name__ == "__main__":
    # Example usage
    input_file = "data/math_questions_filtered.json"
    analyze_error_distribution(input_file)