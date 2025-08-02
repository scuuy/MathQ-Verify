import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Import your API module here
# Example: from your_api_module import call_llm_api

# System prompt
SYSTEM_INFO = "Determine if the following question is a multiple-choice question, respond with only true or false."
input_filename = "path/to/your/input/file.jsonl"  # Previously generated JSON file (list format)
output_filename = "path/to/your/output/file.jsonl"  # Updated JSONL file to write to

# Thread lock for file writing synchronization
write_lock = threading.Lock()

def process_record(record):
    """
    Process a single record:
    1. Construct prompt to call API to determine if the question is multiple-choice
    2. Update the record's choice_question field based on API response
    3. Immediately append the record as a line of JSON to the output file
    """
    question_text = record.get("question", "")
    prompt_text = f"Determine if the following is a multiple-choice question (Question:\n{question_text}\n), respond with only true or false (no additional text)."
    
    # Call API, using model "your-model-name"
    # Replace with your actual API call
    # response = call_llm_api(SYSTEM_INFO, prompt_text, model="your-model-name")
    response = "false"  # Replace with actual API call
    
    # Update field based on response (assuming response contains only true or false)
    if response.strip().lower() == 'true':
        record["choice_question"] = True
    else:
        record["choice_question"] = False

    # Write as a line of JSON to the file
    record_line = json.dumps(record, ensure_ascii=False)
    with write_lock:
        with open(output_filename, 'a', encoding='utf-8') as outfile:
            outfile.write(record_line + "\n")
    
    return record

def main():
    # Read JSON file (list format)
    with open(input_filename, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    
    total = len(data)
    print(f"Read {total} records, starting multi-threaded processing...")

    # Clear output file (to avoid impact from previous data)
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        pass

    # Use thread pool for multi-threaded processing, adjust max_workers as needed
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(process_record, record) for record in data]
        # Use tqdm to monitor task execution progress
        for _ in tqdm(as_completed(futures), total=total, desc="Processing records"):
            pass

    print(f"Processing complete, updated file saved to {output_filename}")

if __name__ == "__main__":
    main()