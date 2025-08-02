import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Import API module
sys.path.append("path/to/api")
from api_client import openai_chat

# Define system prompt with clear output format
SYSTEM_PROMPT = """
You are a classification assistant specialized in mathematics. Your task is to classify the given text into one primary category and one secondary category according to the following taxonomy. Do not output any extra explanation. Your response must be in the following format:
{
    "primary_category": "Your primary category here",
    "secondary_category": "Your secondary category here"
}
for example:
{
    "primary_category": "1. Foundations and Logic",
    "secondary_category": "1.1 Mathematical Logic and Set Theory"
}
here is all primary category and corresponding secondary category of Taxonomy:

1. Foundations and Logic
   1.1 Mathematical Logic and Set Theory
       - Focuses on the study of abstract logical structures and set-based operations.
       - Includes topics such as propositional and predicate logic, logical inference methods, proof techniques, set operations, and related combinatorial reasoning.

   1.2 Basic Theory, Formalization, and History & Education
       - Explores the foundational principles of mathematics through formal systems and the evolution of mathematical thought.
       - Covers areas such as axiomatic systems, formalization of mathematical theories, historical development of mathematics, and approaches to teaching mathematical concepts.

2. Algebra and Number Theory
- 2.1 Linear Algebra and Group Theory
- 2.2 Ring Theory, Field Theory, and Polynomial Algebra
- 2.3 Commutative Algebra and Homological/Categorical Methods
- 2.4 Number Theory
- 2.5 Algebraic Geometry

3. Analysis and Differential Equations
- 3.1 Real Analysis, Measure Theory, and Functional Analysis
- 3.2 Complex Analysis and Special Functions
- 3.3 Differential Equations and Dynamical Systems
- 3.4 Integral Transforms, Integral Equations, and Difference Equations
- 3.5 Harmonic Analysis

4. Geometry and Topology
- 4.1 Euclidean, Analytic, and Convex/Discrete Geometry
- 4.2 Differential Geometry and Manifold Theory
- 4.3 Topology and Algebraic Topology

5. Probability, Statistics, and Discrete Mathematics
- 5.1 Probability Theory and Stochastic Processes
- 5.2 Mathematical Statistics
- 5.3 Combinatorics and Graph Theory

6. Applied and Computational Mathematics
- 6.1 Numerical Analysis and Computational Methods
- 6.2 Optimal Control, Variational Methods, and Optimization
- 6.3 Operations Research and Game Theory
- 6.4 Systems Theory and Control
- 6.5 Computer Science and Algorithms
- 6.6 Mathematical Physics and Engineering Mathematics
- 6.7 Information and Communication
- 6.8 Biomathematics

7. Arithmetic
- 7.1 Arithmetic and Number Operations: Elementary to Advanced
    - Dedicated exclusively to numerical computations and operational techniques.
    - Encompasses basic arithmetic (addition, subtraction, multiplication, division) as well as more advanced computational methods focused solely on numerical processing and calculations.
- 7.2 Word Problems and Real-Life Applications
"""

# File paths
input_file_path = "data/math_questions_filtered.json"
output_file_path = "data/categorized_questions.json"

def build_classification_prompt(question):
    """
    Build a classification prompt for the given question
    :param question: The question text to be classified
    :return: Complete prompt text
    """
    return f"""User Prompt:
Classify the following text into one primary category and one secondary category based on the taxonomy above. The text is:
{question}"""


def classify_single_question(record):
    """
    Process a single record, call API for classification, and return a dictionary with classification results
    :param record: Single record containing question information
    :return: Dictionary with classification results
    """
    question_no = record.get("question_no")
    question = record.get("question", "")
    full_prompt = build_classification_prompt(question)

    try:
        response = openai_chat(SYSTEM_PROMPT, full_prompt, model="gpt-4o")
    except Exception as e:
        response = f"API Error: {e}"
        primary_category = "Unknown"
        secondary_category = "Unknown"
    else:
        # Try to extract JSON part from the response
        start_index = response.find('{')
        end_index = response.rfind('}')
        if start_index != -1 and end_index != -1:
            json_str = response[start_index:end_index + 1]
            try:
                parsed = json.loads(json_str)
                primary_category = parsed.get("primary_category", "Unknown")
                secondary_category = parsed.get("secondary_category", "Unknown")
            except Exception as e:
                primary_category = "Unknown"
                secondary_category = "Unknown"
                response = f"Response format error: {e}"
        else:
            primary_category = "Unknown"
            secondary_category = "Unknown"
            response = "Could not find valid JSON in response"

    return {
        **record,
        "primary_category": primary_category,
        "secondary_category": secondary_category,
        "classification_response": response
    }


def main():
    try:
        # Read input file
        with open(input_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        results = []
        max_workers = 30  # Adjust thread count as needed

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(classify_single_question, record) for record in data]
            for future in tqdm(as_completed(futures), total=len(futures), desc="Classifying Questions"):
                result = future.result()
                results.append(result)
                # Optional delay
                time.sleep(0.1)

        # Save processed data to new file
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        print(f"Successfully classified questions and saved to {output_file_path}")

    except FileNotFoundError:
        print(f"Input file not found: {input_file_path}")
    except Exception as e:
        print(f"Error processing file: {e}")


if __name__ == "__main__":
    main()