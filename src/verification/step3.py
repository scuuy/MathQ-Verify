import json
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Import your API module here
# Example: from api_utils import openai_chat
from api_utils import openai_chat

# Define system prompt
SYSTEM_PROMPT = (
    "You are an expert in evaluating mathematical problems. "
    "Follow the user's instructions strictly and output your final judgment in the required JSON format."
)

def build_step3_prompt(question):
    """
    Build the prompt for step 3 verification: checking for contradictions between minimal conditions
    or unreasonable answers.
    
    Args:
        question (str): The mathematical problem to evaluate
        
    Returns:
        str: The formatted prompt for the LLM
    """
    prompt = f"""You are given a mathematical problem. Perform the following step:
3. Check if there are any contradictions between the minimal conditions stated in the problem (that cannot be further decomposed), or if the possible answers are unreasonable.
   Do not consider whether the individual conditions violate the mathematical domain.

After performing this step, output your final judgment in JSON format with exactly the following keys:
{{
    "judgement_test": true/false,
    "error_type": "<error description or null>"
}}
You may include your chain-of-thought, but the final answer must be the JSON object above.

Here is the problem to evaluate:
-------------------------------
{question}
-------------------------------
"""
    return prompt

def determine_gt(record):
    """
    Determine the ground truth judgment based on the contradiction_check field.
    
    Args:
        record (dict): The record containing annotation fields
        
    Returns:
        bool: The ground truth judgment
    """
    return record.get("contradiction_check", False)

def process_record(record):
    """
    Process a single record by calling the API to perform step 3 verification.
    
    Args:
        record (dict): The record containing the question to evaluate
        
    Returns:
        dict: The result of the verification
    """
    question_no = record.get("question_no")
    question = record.get("question")
    judgement_gt = determine_gt(record)

    full_prompt = build_step3_prompt(question)
    try:
        # Replace with your preferred model
        response = openai_chat(SYSTEM_PROMPT, full_prompt, model="gpt-4")
    except Exception as e:
        response = f"API Error: {e}"
        judgement_test = False
        error_type = "API call failed"
    else:
        start_index = response.find('{')
        end_index = response.rfind('}')
        if start_index != -1 and end_index != -1 and start_index < end_index:
            json_str = response[start_index:end_index + 1]
            try:
                parsed = json.loads(json_str)
                judgement_test = parsed.get("judgement_test", False)
                error_type = parsed.get("error_type", None)
            except Exception as e:
                # JSON-like structure found but parsing failed
                judgement_test = False
                error_type = "Response format error: " + str(e)
        else:
            # No suitable JSON structure found
            judgement_test = False
            error_type = "Response format error: No valid JSON found"

    return {
        "question_no": question_no,
        "question": question,
        "judgement_gt": judgement_gt,
        "judgement_test": judgement_test,
        "error_type": error_type,
        "response": response
    }

def main():
    # Set input and output file paths
    input_file = "data/contradiction_check_false.json"  # Replace with your input file path
    output_file = "results/step3.json"  # Replace with your output file path

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []
    max_workers = 30  # Adjust the number of threads as needed

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_record, record) for record in data]
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing Step 3"):
            result = future.result()
            results.append(result)
            # Optional delay to avoid API rate limits
            time.sleep(0.1)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Step 3 testing results have been saved to {output_file}")

if __name__ == "__main__":
    main()