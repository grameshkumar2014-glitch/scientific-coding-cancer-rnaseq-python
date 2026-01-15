# Scientific Coding – Cancer RNA-Seq Analysis (Python)

## Overview
This repository presents a research-grade scientific coding project in
computational biology using Python.

The goal is to demonstrate:
- Graduate-level problem formulation
- Statistically sound differential expression analysis
- Validation beyond basic p-values
- Evidence-based comparison with a published RNA-Seq cancer study

This project is designed as a portfolio example for Scientific Coding roles.

---

## Scientific Problem
Given:
- A gene-level RNA-Seq count matrix
- Sample metadata including biological condition and batch

Design and implement a Python-based workflow to:
1. Normalize expression data
2. Identify differentially expressed genes
3. Control false discovery rates
4. Validate robustness using permutation testing
5. Compare results with published findings

---

## How to Run
```bash
pip install -r requirements.txt
python src/differential_expression.py
python validation/permutation_test.py
Notes
No raw FASTQ or patient-identifiable data included

All results are methodologically justified

No claims exceed statistical evidence

Author

Dr Ramesh Kumar Gopal