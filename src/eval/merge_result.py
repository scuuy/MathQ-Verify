import json

def merge_test_results(main_file_path, step_files, output_file_path):
    """Merge test results from multiple step files into a single comprehensive result file"""
    def load_data(file_path):
        """Load data from a JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []

    # Load main file data
    main_data = load_data(main_file_path)
    # Load data from each step file
    all_step_data_list = [load_data(file_path) for file_path in step_files]

    # Build dictionaries of step data by question_no
    step_data_dict_list = []
    for step_data in all_step_data_list:
        step_dict = {item.get('question_no'): item for item in step_data}
        step_data_dict_list.append(step_dict)

    # Merge data
    combined_data = []
    for item in main_data:
        question_no = item.get('question_no')
        new_item = item.copy()
        step_results = []

        for i, step_dict in enumerate(step_data_dict_list):
            step_item = step_dict.get(question_no, {})
            step_key = f"step{i + 1}_test"
            error_type_key = f"step{i + 1}_error_type"
            new_item[step_key] = step_item.get("judgement_test")
            new_item[error_type_key] = step_item.get("error_type")
            step_results.append(step_item.get("judgement_test"))

        # Create final test_result
        new_item['test_result'] = all(step_results) if step_results else False

        combined_data.append(new_item)

    # Save merged data to new file
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, ensure_ascii=False, indent=2)
        print(f"Data successfully merged and saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
        
    return combined_data


if __name__ == "__main__":
    # Example usage
    main_file = "data/math_questions_with_ground_truth.json"
    step_files = [
        "data/step1_results.json",
        "data/step2_results.json",
        "data/step3_results.json",
        "data/step4_results.json"
    ]
    output_file = "results/combined_test_results.json"
    merge_test_results(main_file, step_files, output_file)