# ROMEBiasedExperiment

This repository explores bias behavior in language models using the ROME (Rank-One Model Editing) method. It contains experiments analyzing how model edits interact with biased knowledge representations.

# Overview
ROME (Rank-One Model Editing) is a technique used to modify factual knowledge in transformer-based language models by applying a targeted rank-one update to model weights.
This project investigates:
How ROME edits influence biased outputs
Whether bias persists, amplifies, or shifts after edits
The stability of edits across different prompts

# Key Concepts
1. ROME (Rank-One Model Editing): A method for editing specific factual associations in large language models
2. Bias in LLMs: Systematic skew in model outputs toward certain demographics or stereotypes
3. Causal Tracing: Identifying which internal components of a model contribute to a prediction

# Pipelines
1. Setup and clone repo
2. Imports
3. Load tokenizer and model
4. Patch tokenizer padding
5. Any repo compatibility fixes
6. Sanity check
7. Dataset
8. Helper functions
9. Full experiment loop
10. Save CSV
11. Summary
12. Download CSV

# Acknowledgements & References
This project is adapted and modified from the original ROME implementation:
ROME GitHub Repository
The original repository provides an implementation of Rank-One Model Editing for transformer models, including GPT-2 and GPT-J ().
This work extends the original implementation to explore bias-related behaviors under model editing, tailored for experimental and research purposes.
If you use this repository, please also cite the original 
ROME paper:
Meng et al., Locating and Editing Factual Associations in GPT (NeurIPS 2022)
