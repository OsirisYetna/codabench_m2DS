
<div align="center">
    <img src="logo.png" alt="Logo" width="25%">
</div>

# **Challenge : Molecular Property Prediction**

___
*Matthieu Kaeppelin (M2DS)*

*Bastien Lecomte (M2DS)*

*Antoine Verier (M2DS)*

*Thomas Vujasinovic (M2DS)*

*Kam Osiris Yetna (M2DS)*
___
# Introduction


- The data for this challenge comes from a subset of the MoleculeNet dataset, a globally recognized benchmark for evaluating machine learning algorithms in chemistry.

- More specifically, this challenge is based on the `molvision/BACE-V-SMILES-0` dataset. It contains SMILES representations (*Simplified Molecular-Input Line-Entry System*) of a large set of chemical compounds, which have been experimentally tested in vitro to assess their ability to inhibit the Beta-secretase 1 enzyme (BACE-1).

### **What is the objective of the task ?** 

Your mission is to design a robust binary classification model. Your algorithm will take the SMILES string of a molecule as input and predict its efficacy as a BACE-1 inhibitor by assigning it a label:

- Label = 1: The molecule is an active inhibitor of BACE-1.

- Label = 0: The molecule is inactive.

### **Why does it matters ?**

The enzyme BACE-1 plays a central role in the formation of amyloid plaques in the brain, one of the main pathological characteristics of Alzheimer's disease. It is therefore a major therapeutic target.
However, developing a new drug is an extremely cumbersome process. Physically testing millions of chemical compounds in the laboratory is an impossible approach on a large scale.

This is where machine learning becomes crucial. Being able to predict the activity of these inhibitors computationally (in silico) makes it possible to quickly filter candidate molecules, drastically reduce clinical failures, and accelerate the discovery of new treatments.

### **Out-of-distribution test set**

This is not a standard random-split challenge. The dataset has been strictly split based on Molecular Weight (MW):

- Train set: it contains smaller molecules (MW < 592 Da).

- Hidden test set: it contains exclusively larger molecules (MW ≥ 592 Da).

Your model must prove it has learned true chemical rules to extrapolate to uncharted chemical space, rather than just memorizing the training statistics! 

***NB** : You are not allowed to use the molecules of the hidden test set for training or validation. Any attempt to do so will lead to disqualification.*

### **First steps to help you get started:**

To manipulate the chemical data in the challenge, we strongly recommend using RDKit, the leading Python library for chemoinformatics. Its `Chem` module will allow you to easily convert SMILES text strings into more manageable molecular objects, then generate numerical descriptors (such as Morgan Fingerprints) that can be directly used by your machine learning models. RDKit is a powerful tool that will greatly facilitate your task of extracting the relevant characteristics of your molecules and climbing to the top of the rankings! 

RDKit documentation: https://www.rdkit.org/docs/GettingStartedInPython.html


# Evaluation metric
Submissions are evaluated using **Cohen’s Kappa** score. This metric is robust to class imbalance and accounts for agreement occurring by chance, which makes it more appropriate than raw accuracy for this dataset.

# Baseline model
A baseline is provided in the notebook using:

- **Morgan fingerprints** (ECFP-like) from RDKit
- **Random forest** classifier

This baseline converts SMILES to fixed-length fingerprints, then trains a Random Forest to predict labels. The socre is approximately 0.31, TRY TO BEAT IT!

# Submission format

Your submission file should be `.py` file containging a scikit-learn compatible estimator class with  `fit`, `predict` and `predict_proba` methods. You can find an example implementation in the `solution/submission.py` file.

# Tips for better performance
- Try molecular featurization beyond Morgan fingerprints (e.g., RDKit descriptors, graph neural networks)
- Use probability calibration to improve decision thresholds
- Consider model robustness to the OOD split (e.g., domain adaptation or regularization)

---

