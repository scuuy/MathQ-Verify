import json

# Define input file paths
input_step1_file = "path/to/your/step1.json"
input_original_file = "path/to/your/original_data.json"
# Define output file path
output_file = "path/to/your/updated_step1.json"

# Read step1.json file
with open(input_step1_file, "r", encoding="utf-8") as f:
    step1_results = json.load(f)

# Read original data file
with open(input_original_file, "r", encoding="utf-8") as f:
    original_data = json.load(f)

# Create a mapping with question_no as key and level_0_check as value
level_0_check_mapping = {record["question_no"]: record["level_0_check"] for record in original_data}

# Update judgement_gt values in step1.json
for result in step1_results:
    question_no = result["question_no"]
    if question_no in level_0_check_mapping:
        result["judgement_gt"] = level_0_check_mapping[question_no]

# Save updated results to new file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(step1_results, f, ensure_ascii=False, indent=2)

print(f"Updated results saved to {output_file}")