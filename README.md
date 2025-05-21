# 🚀 MathQ-Verify: Let's Verify Math Questions Step by Step  
<div align="center">

**[📄 arXiv Paper](https://arxiv.org/abs/2505.13903 ) | [📊 ValiMath Dataset](https://huggingface.co/datasets/scuuy666/ValiMath )**

</div>

## 🔥 News
- 📁 **2025-05-21**: The **ValiMath dataset** is now publicly available on [Hugging Face](https://huggingface.co/datasets/scuuy666/ValiMath).
---

## 🌟 Overview  
Large Language Models (LLMs) often generate **math problems with hidden flaws** (e.g., contradictions, missing premises). To address this, we propose **MathQ-Verify**, a **five-stage pipeline** to rigorously filter ill-posed math questions and ensure dataset reliability.  

---

## 🔍 Key Contributions  
1. **MathQ-Verify Framework**  
   - Detects contaminated instructions, linguistic errors, atomic condition flaws, logical contradictions, and completeness gaps.  
   - Achieves **90% precision** and **63% recall** via lightweight model voting.  

2. **ValiMath Benchmark** 📊 
   - 2,147 math questions with **fine-grained stepwise validity labels** (5 error types).  
   - [Hugging Face Link 🤗](https://huggingface.co/datasets/scuuy666/ValiMath)  

3. **Comprehensive Evaluation** 📈  
   - Improves F1 score by **15%** over baselines on ValiMath.  
   - Ablation studies validate each verification stage's necessity.  

---

## 🧩 Framework  
![Framework](images/overview.jpg)  

---

## 📦 ValiMath Dataset  
**[Explore on Hugging Face 🤗](https://huggingface.co/datasets/scuuy666/ValiMath)**  
- **2,147** problems (1,299 correct, 848 incorrect).  
- **5 Error Types**: Contradictions, incompleteness, domain mismatches, etc.  
- **Stepwise Annotations**: Per-step validity labels for thorough analysis.  

---

## 🛠️ Usage  

The code are being finalized at full speed and will be uploaded soon.🙂
<!-- ```bash
# Clone the repo
git clone https://github.com/scuuy/MathQ-Verify.git
cd MathQ-Verify

# Install dependencies
pip install -r requirements.txt

# Run verification pipeline
python mathq_verify.py --input your_math_questions.json
``` -->

---


## 📚 Citation  
```bibtex
@misc{shen2025letsverifymathquestions,
      title={Let's Verify Math Questions Step by Step}, 
      author={Chengyu Shen and Zhen Hao Wong and Runming He and Hao Liang and Meiyi Qiang and Zimo Meng and Zhengyang Zhao and Bohan Zeng and Zhengzhou Zhu and Bin Cui and Wentao Zhang},
      year={2025},
      eprint={2505.13903},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.13903}, 
}
```

---

## 🧠 Contact  
For questions or feedback, open an issue on GitHub or email [scuuy05@gmail.com](mailto:scuuy05@gmail.com).  
*Let’s build reliable math datasets together! 🚀*