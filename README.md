<div align="center">

# 🚀 MathQ-Verify

</div>

## 🔥 News
- 📁 The **ValiMath dataset** has been released for research use.
- 🧩 The **source code** is now available for the research community!

## 🌟 Overview  
Large Language Models (LLMs) often generate **math problems with hidden flaws**, such as contradictions or missing premises. To address this issue, we propose **MathQ-Verify**, a **five-stage pipeline** designed to rigorously filter ill-posed math questions and improve the overall quality of math datasets.

## 🔍 Key Contributions  
1. **MathQ-Verify Framework**  
   - Detects various types of errors in math problems: contaminated instructions, linguistic errors, atomic condition flaws, logical contradictions, and completeness gaps.  
   - Achieves **90% precision** and **63% recall** using lightweight model voting strategies.  

2. **ValiMath Benchmark** 📊 
   - Contains **2,147 math questions** with **fine-grained stepwise validity labels** across **5 error categories**.  

3. **Comprehensive Evaluation** 📈  
   - Outperforms baseline methods by **+15% in F1 score** on the ValiMath benchmark.
   - Ablation studies demonstrate the effectiveness of each verification stage.

## 🧩 Framework  
![Framework](images/overview.jpg)

## 📦 Dataset Overview  
We provide a high-quality dataset for evaluating math question validity. It includes:
- **2,147** math problems in total (split into correct and incorrect subsets).
- Each problem is annotated with **step-by-step validity labels**.
- Supports detailed analysis of error types such as **contradictions**, **incompleteness**, and **domain mismatches**.

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/MathQ-Verify.git
cd MathQ-Verify

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Quick Start Guide

### 1. Dataset Exploration

The ValiMath dataset is provided in JSONL format with each entry containing:
- Question text
- Validity labels for each verification step
- Category and difficulty information

```bash
# View dataset statistics
python src/draw/distribution.py
```

### 2. Running the Verification Pipeline

The verification pipeline consists of 5 sequential steps:

```bash
# Step 0: Check if the input is a proper math problem
python src/verification/step0.py --input path/to/your/questions.json --output results/step0_results.json

# Step 1: Check for linguistic errors
python src/verification/step1.py --input results/step0_results.json --output results/step1_results.json

# Step 2: Check for atomic condition flaws
python src/verification/step2.py --input results/step1_results.json --output results/step2_results.json

# Step 3: Check for logical contradictions
python src/verification/step3.py --input results/step2_results.json --output results/step3_results.json

# Step 4: Check for completeness
python src/verification/step4.py --input results/step3_results.json --output results/step4_results.json
```

### 3. Classifying Your Math Questions

```bash
# Classify by category
python src/classification/category.py --input path/to/your/questions.json --output results/category_results.json

# Classify by difficulty
python src/classification/difficulty.py --input path/to/your/questions.json --output results/difficulty_results.json
```

### 4. Evaluating Results

```bash
# Calculate metrics for a single verification step
python src/eval/metrics.py --input results/step4_results.json

# Merge results from all steps and apply voting
python src/eval/merge_result.py --input_dir results/ --output results/merged_results.json
python src/eval/voting.py --input results/merged_results.json --output results/final_results.json

# Calculate metrics across multiple files
python src/eval/multifile_metrics.py --input_dir results/
```

## 📋 Input Format

Your input file should be a JSON or JSONL file with each entry containing at least:

```json
{
  "question_no": 1,
  "question": "Your math question text here"
}
```

## 🔧 Customization

- Modify the API settings in each verification step file to use your preferred LLM.
- Adjust the prompts in each step to fit your specific requirements.
- Configure voting strategies in `src/eval/voting.py` to optimize for precision or recall.

## 📚 Citation  
If you find our work useful in your research, please cite:

```bibtex
@misc{anonymous2025mathqverify,
      title={Let's Verify Math Questions Step by Step}, 
      author={Anonymous Authors},
      year={2025},
      note={Under review}
}
```

---

## 🧠 Contact  
This repository is anonymized for review. Please check back after the review process for more information.

*Let's build reliable math datasets together! 🚀*

---

> ✅ **Note**: Some features may be updated as we continue to improve the codebase. Please check for updates regularly.