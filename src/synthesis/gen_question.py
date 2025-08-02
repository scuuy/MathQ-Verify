import json
import os
import sys
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Import your API module here
# Example: from your_api_module import call_llm_api

# Configuration (modify as needed)
MODEL = "your-model-name"  # Replace with your model name
DATA_FILE = "path/to/your/input/data.json"  # Input file path
OUTPUT_FILE = "path/to/your/output/data.jsonl"  # Output file path, one JSON object per line
NEW_Q_NUM = 5  # Number of new questions to generate per original question

# Diversity mode list, can be extended or adjusted as needed
diversity_mode = [
    "1, 2, 3",
    "1, 2, 4",
    "1, 2, 5",
    "1, 4, 5",
    "1, 2, 3, 4, 5"
]

# Prompt template
used_prompt = """
Create a new reasonable and solvable math problem from the original problem by applying some of the following transformations (focus on all the transformations of "{items}"):

1. Alter numerical values or expressions, ensuring the new problem remains solvable.
2. Modify the problem type: introduce concepts like ratios or percentages, switch between derivatives and integrals, change the question from finding an area to finding a perimeter, etc.
3. Contextualize the problem within a real-world scenario, such as incorporating various payment methods or deferred payments with interest.
4. Add additional premises that require considering an extra factor separately in solving the problem.
5. Increase the complexity of the problem by introducing multiple conditions that necessitate case-by-case analysis for a solution.

Here is the problem from the user:
{question}
Write another problem inspired by this one.
Not only change the problem scenario, but also try to create a new problem that requires another approach to solve.
Start directly with the problem statement and DO NOT include any phrases such as "Here is a new problem inspired by a given one".
After the problem is generated finish your response right away.
"""

# System prompt
sys_prompt = '''You are an intelligent chatbot designed for writing another solvable math question from given question and answer.
Remember: DO NOT output anything else such as "To create a new math problem similar to the given one...", only output the new question you make.'''

# Write lock to ensure thread-safe file writing
write_lock = threading.Lock()

def generate_synthetic_question(original_question, mode_iter):
    """Generate a single synthetic question, return the generated string."""
    # Select diversity mode (cycle through them)
    diversity = diversity_mode[mode_iter % len(diversity_mode)]
    # Format user prompt
    user_prompt = used_prompt.replace("{question}", original_question).replace("{items}", diversity)
    # Call API to generate synthetic question
    # Replace this with your actual API call
    # synthetic_question = call_llm_api(sys_prompt, user_prompt, model=MODEL)
    synthetic_question = "Example synthetic question"  # Replace with actual API call
    # Simulate delay to prevent API calls from being too frequent
    time.sleep(random.uniform(1, 2))
    return synthetic_question

def process_item(item):
    """Generate multiple synthetic questions for one original question, and write to output file immediately after each API return."""
    original_question = item.get("problem", "")
    for mode_iter in range(NEW_Q_NUM):
        synthetic_question = generate_synthetic_question(original_question, mode_iter)
        result = {
            "source": item.get("source", ""),
            "original_question": original_question,
            f"synthetic_question_{mode_iter+1}": synthetic_question
        }
        # Write each result to the output file immediately
        with write_lock:
            with open(OUTPUT_FILE, "a", encoding="utf-8") as outfile:
                json.dump(result, outfile, ensure_ascii=False)
                outfile.write("\n")
                outfile.flush()

def load_jsonl(file_path):
    """Read jsonl file, one JSON object per line, return a list."""
    items = []
    with open(file_path, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    items.append(json.loads(line))
                except Exception as e:
                    print(f"Parse error: {e}, content: {line}")
    return items

def main():
    # Load input data (jsonl format, one JSON object per line)
    data = load_jsonl(DATA_FILE)
    total_tasks = len(data)
    print(f"Found {total_tasks} records, starting to generate synthetic questions...")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE) or ".", exist_ok=True)
    
    # Use ThreadPoolExecutor for multi-threaded processing
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(process_item, item) for item in data]
        # Use tqdm to display progress bar
        for _ in tqdm(as_completed(futures), total=total_tasks, desc="Generation progress"):
            pass  # Just update progress bar, no additional processing needed
    print("Synthetic question generation complete, results saved to:", OUTPUT_FILE)

if __name__ == "__main__":
    main()