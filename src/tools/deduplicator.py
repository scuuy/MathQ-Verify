import json

# Read JSON file
file_path = 'path/to/your/data.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Count duplicates in the 'question' field
question_counts = {}
for item in data:
    question = item['question']
    if question in question_counts:
        question_counts[question] += 1
    else:
        question_counts[question] = 1

# Find duplicate questions and their counts
duplicate_questions = {q: count for q, count in question_counts.items() if count > 1}

# Output results
print(f"Number of duplicate questions: {len(duplicate_questions)}")
for question, count in duplicate_questions.items():
    print(f"Question: {question[:100]}...(truncated due to length limit)")
    print(f"Duplicate count: {count}")
    print("-" * 50)